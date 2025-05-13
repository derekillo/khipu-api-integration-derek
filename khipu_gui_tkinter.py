
# Importa la biblioteca Tkinter para crear la interfaz gráfica
import tkinter as tk
# messagebox permite mostrar mensajes emergentes de información o error
from tkinter import messagebox
import requests
import webbrowser
from datetime import datetime
import re

# Validación simple de formato de correo

# Función que valida si el correo tiene un formato correcto mediante expresión regular
def es_correo_valido(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo)


# Función que se ejecuta al presionar el botón 'Crear Pago'
def generar_pago():
    monto = entry_monto.get()
    descripcion = entry_descripcion.get()
    correo = entry_correo.get()

    # Validaciones
    if not monto.isdigit() or int(monto) <= 0:
        messagebox.showerror("Error", "El monto debe ser un número mayor a 0.")
        return
    if not descripcion.strip():
        messagebox.showerror("Error", "La descripción no puede estar vacía.")
        return
    if not correo.strip() or not es_correo_valido(correo):
        messagebox.showerror("Error", "El correo ingresado no es válido.")
        return

    transaction_id = "tx-" + datetime.now().strftime("%Y%m%d%H%M%S")
    url = "https://payment-api.khipu.com/v3/payments" # URL de la API de Khipu
    headers = {
        "x-api-key": "fc71c0f5-1efe-4f5e-9cdc-080ef55d8535", # Reemplaza con tu API Key
        "Content-Type": "application/json"
    }
    data = {
        "amount": int(monto),
        "currency": "CLP",
        "subject": descripcion,
        "payer_email": correo,
        "transaction_id": transaction_id,
        "return_url": "https://www.khipu.com/",
        "cancel_url": "https://www.khipu.com/"
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        pago = response.json()
        webbrowser.open(pago["payment_url"])
        messagebox.showinfo("Pago creado", f"✅ Pago creado exitosamente.\n\nURL: {pago['payment_url']}")
    else:
        messagebox.showerror("Error", f"No se pudo crear el pago.\nCódigo: {response.status_code}\n{response.text}")

# Crear la ventana principal de la aplicación
# Inicializa la ventana de Tkinter
app = tk.Tk()
app.title("Generar Pago - Khipu")
app.geometry("400x250")

tk.Label(app, text="Monto (CLP):").pack(pady=(10, 0))
entry_monto = tk.Entry(app)
entry_monto.pack()

tk.Label(app, text="Descripción del pago:").pack(pady=(10, 0))
entry_descripcion = tk.Entry(app)
entry_descripcion.pack()

tk.Label(app, text="Correo del pagador:").pack(pady=(10, 0))
entry_correo = tk.Entry(app)
entry_correo.pack()

tk.Button(app, text="Crear Pago", command=generar_pago).pack(pady=20)

# Ejecuta el bucle principal de la aplicación
app.mainloop()
