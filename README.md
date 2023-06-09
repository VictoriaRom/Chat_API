# CHAT API

La API ChatGPT-Python es una interfaz basada en Flask que se conecta con el modelo de lenguaje de ChatGPT de OpenAI. Permite a los usuarios enviar mensajes y recibir respuestas generadas por el modelo de lenguaje.

## Descripción

La API ChatGPT-Python proporciona una forma sencilla de interactuar con el modelo de lenguaje de ChatGPT utilizando solicitudes HTTP. Al enviar un mensaje a través de la API, se generará una respuesta utilizando el modelo de lenguaje y se devolverá al usuario.

Esta API puede ser utilizada en diversos casos de uso, como chatbots, asistentes virtuales, sistemas de preguntas y respuestas, entre otros.

## Características

- Interfaz simple: La API ofrece una interfaz HTTP sencilla para enviar mensajes y recibir respuestas generadas por el modelo de lenguaje de ChatGPT.
- Personalización: Puedes adaptar y ajustar los parámetros de la conversación según tus necesidades específicas.
- Escalabilidad: La API se puede escalar fácilmente para manejar cargas de trabajo de diferentes tamaños y volúmenes de solicitudes.

## Documentación y uso

Para utilizar la API ChatGPT-Python, sigue estos pasos:

1. Clona o descarga el repositorio en tu máquina local.
2. Asegúrate de tener las dependencias necesarias instaladas. Puedes instalarlas ejecutando `pip install -r requirements.txt`.
3. Ejecuta el archivo `app.py` para iniciar el servidor Flask.
4. Realiza solicitudes POST a la URL `http://localhost:5000/chat` para enviar mensajes y recibir respuestas generadas por ChatGPT.

### Ejemplo de solicitud

```
POST /chat HTTP/1.1
Host: localhost:5000
Content-Type: application/json

{
    "message": "Hola, ¿cómo estás?"
}
```

### Ejemplo de respuesta

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "response": "Hola, estoy bien. ¿En qué puedo ayudarte?"
}
```

## Contribución

Si deseas contribuir a este proyecto, puedes seguir los siguientes pasos:

1. Realiza un fork del repositorio en GitHub.
2. Crea una rama con una descripción clara de la mejora o función que estás implementando.
3. Realiza los cambios y las pruebas necesarias en tu rama local.
4. Envía una solicitud de pull para fusionar tus cambios en la rama principal del repositorio.

## Créditos

La API ChatGPT-Python fue desarrollada por Victoria Romero.
