
# 💳 Integración API de Pagos Khipu - Prueba Técnica

Este repositorio contiene la solución desarrollada por **Derek Needham** para la prueba técnica del cargo *Customer Success (con enfoque técnico)* en **Khipu**. El objetivo fue realizar una integración con la API de pagos usando el entorno de pruebas (DemoBank).

---

## ✅ Descripción del desafío

> Se solicitó simular una integración real utilizando únicamente llamadas a la API de Khipu (no cobros creados desde el portal), generando un pago funcional con monto de prueba y verificando su conciliación.

---

## 📂 Archivos incluidos

| Archivo | Descripción |
|--------|-------------|
| `khipu_test.py` | Versión de consola, 100% interactiva desde terminal. |
| `khipu_gui_tkinter.py` | Versión con interfaz gráfica (GUI) utilizando Tkinter. |
| `README.md` | Este documento con instrucciones y explicación técnica. |
| `evidencias/` | Carpeta sugerida para agregar capturas del proceso completo. |

---

## ⚙️ Requisitos

- Python 3.8 o superior
- Paquete `requests` → instalar con `pip install requests`
- Tkinter → viene incluido con la mayoría de distribuciones de Python

---

## 🧪 Cómo ejecutar

### Consola (modo texto)
```bash
python khipu_test.py
```

### Interfaz gráfica (Tkinter)
```bash
python khipu_gui_tkinter.py
```

---

## 🔄 Flujo implementado

1. Se solicita al usuario el monto, motivo y correo del pagador.
2. Se genera un `transaction_id` único con marca de tiempo.
3. Se envía una solicitud `POST /v3/payments` a la API.
4. Se abre el navegador automáticamente con la URL de pago.
5. El pago se realiza usando DemoBank (simulación).
6. Se puede verificar el estado del pago con `GET /payments/{payment_id}` (Postman).
7. Se comprueba conciliación con:
   - `"status": "done"`
   - `conciliation_date` válido

---

## 📚 Referencias usadas (documentación oficial Khipu)

- [Crear cobro con API](https://docs.khipu.com/portal/es/payment-api/#crear-un-cobro)
- [Autenticación API Key](https://docs.khipu.com/portal/es/payment-auth/)
- [Verificar pago - GET payment_id](https://docs.khipu.com/openapi/es/v1/instant-payment/openapi/operation/getPaymentById/)

---

## 📸 Evidencias

Se recomienda incluir capturas de:
- Script en ejecución
- Pago realizado en navegador
- Postman mostrando conciliación del pago

---

## 🧠 Comentario final

Este proyecto fue desarrollado con enfoque en la comprensión técnica del producto, uso correcto de la API REST, validación de flujo completo y aplicación realista de los recursos de integración.

Gracias por la oportunidad.
