
import requests
import webbrowser
from datetime import datetime
import re

# Función para validar que el correo tenga un formato correcto
def es_correo_valido(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo)

# Función principal que guía el flujo de creación de un pago
def crear_pago():
    print("\n--- Crear pago con Khipu (Modo desarrollador) ---")

    # Paso 1: Solicita un monto válido (entero mayor a cero)
    while True:
        try:
            monto = int(input("💰 Ingresa el monto a pagar (en CLP): "))
            if monto <= 0:
                print("⚠️ El monto debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("⚠️ Error: El monto debe ser un número entero.")

    # Paso 2: Solicita una descripción no vacía
    while True:
        descripcion = input("📝 Ingresa el motivo del pago (o escribe 'cancelar' para salir): ").strip()
        if descripcion.lower() == "cancelar":
            print("🚫 Operación cancelada por el usuario.")
            return
        if not descripcion:
            print("⚠️ La descripción no puede estar vacía.")
        else:
            break

    # Paso 3: Solicita un correo válido con opción de cancelar
    while True:
        correo = input("📧 Ingresa el correo del pagador (o escribe 'cancelar' para salir): ").strip()
        if correo.lower() == "cancelar":
            print("🚫 Operación cancelada por el usuario.")
            return
        if not correo:
            print("⚠️ El correo no puede estar vacío.")
        elif not es_correo_valido(correo):
            print("⚠️ El correo ingresado no tiene un formato válido.")
        else:
            break

    # Paso 4: Genera un identificador único de la transacción
    transaction_id = "tx-" + datetime.now().strftime("%Y%m%d%H%M%S")

    # Paso 5: Define el endpoint y las cabeceras de autenticación
    url = "https://payment-api.khipu.com/v3/payments"
    headers = {
        "x-api-key": "fc71c0f5-1efe-4f5e-9cdc-080ef55d8535",
        "Content-Type": "application/json"
    }

    # Paso 6: Construye el cuerpo de la solicitud con los datos necesarios
    data = {
        "amount": monto,
        "currency": "CLP",
        "subject": descripcion,
        "payer_email": correo,
        "transaction_id": transaction_id,
        "return_url": "https://www.khipu.com/",
        "cancel_url": "https://www.khipu.com/"
    }

    # Paso 7: Realiza la solicitud POST a la API de Khipu
    response = requests.post(url, headers=headers, json=data)

    # Paso 8: Procesa y muestra el resultado
    print("\n--- Resultado ---")
    if response.status_code == 200:
        pago = response.json()
        print("✅ ¡Pago creado con éxito!")
        print("🔗 URL de pago:", pago["payment_url"])
        print("🧾 transaction_id:", transaction_id)
        print("🌐 Abriendo el navegador...")
        webbrowser.open(pago["payment_url"])
        print("🔍 Puedes completar el pago en la página que se abrió en tu navegador.")
    else:
        print("❌ Error al crear el pago.")
        print("Código:", response.status_code)
        print("Detalle:", response.text)

# Ejecuta la función si se llama directamente el script
if __name__ == "__main__":
    crear_pago()
