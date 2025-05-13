
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

## 🔑 Credenciales utilizadas

Se utiliza una cuenta de cobro en **modo desarrollador**, autenticada mediante **API Key** mediante cabecera `x-api-key`.

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

### Consola (modo texto)

Simulación de la ejecución desde terminal, mostrando el ingreso de datos, validación y respuesta de la API:

![image](https://github.com/user-attachments/assets/3aaa425d-2243-4f3b-81a0-a82751e5b68f)
![image](https://github.com/user-attachments/assets/e1c386d7-213a-4212-ab9e-1354cf1b187f)
![image](https://github.com/user-attachments/assets/3383a90f-e4a7-4ad6-8671-e2b0630efcc2)
![image](https://github.com/user-attachments/assets/94784b37-19dd-4102-95f4-545dbbf15f6c)
![image](https://github.com/user-attachments/assets/ec4f2ab8-1f22-4007-a230-8398a2622dc1)
![image](https://github.com/user-attachments/assets/120a8ef9-84ed-4c26-b090-18250c97f4d6)
![image](https://github.com/user-attachments/assets/6d788e8c-f7ff-4060-b4f5-5c3f932c5386)

### Interfaz gráfica (Tkinter)

Simulación de la ventana interactiva con campos de entrada y respuesta visual tras crear el pago:

![image](https://github.com/user-attachments/assets/a93b2919-0fb0-4428-81de-1c49b8bd4d27)
![image](https://github.com/user-attachments/assets/a9dda2c7-ffb0-45c8-8ca3-b65c2c88493f)
![image](https://github.com/user-attachments/assets/99a4037e-a53e-47ca-8adc-047ae2b48680)
![image](https://github.com/user-attachments/assets/b91d473d-e161-43a7-8b07-ede18d8cdccd)
![image](https://github.com/user-attachments/assets/307d76f9-777b-4857-88ce-f58b6a554060)
![image](https://github.com/user-attachments/assets/4c624614-6bce-4663-a659-83a84f903de4)
![image](https://github.com/user-attachments/assets/47c83b5d-830e-40de-a414-89dd503fe9bb)


### Consultar estado de un pago (opcional)

Se puede consultar el estado de un pago en Postman o Python utilizando el endpoint:
```bash
GET https://payment-api.khipu.com/v3/payments/{payment_id}
```

Con el header:
```bash
x-api-key: TU_API_KEY
```

---

## 🧠 Comentario final

Este proyecto fue desarrollado con enfoque en la comprensión técnica del producto, uso correcto de la API REST, validación de flujo completo y aplicación realista de los recursos de integración.

Gracias por la oportunidad.
