from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Configura tu clave de API de OpenAI
openai.api_key = '123clave'

# Ruta para recibir las solicitudes POST
@app.route('/chat', methods=['POST'])
def chat():
    # Obtiene el mensaje del cuerpo de la solicitud
    message = request.json['message']

    # Llama a la función de ChatGPT para obtener la respuesta
    response = chat_gpt(message)

    # Devuelve la respuesta en formato JSON
    return jsonify({'response': response})

def chat_gpt(message):
    # Establece los parámetros para la llamada a OpenAI
    params = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'},
                    {'role': 'user', 'content': message}]
    }

    # Realiza la llamada a OpenAI para obtener la respuesta
    response = openai.ChatCompletion.create(**params)

    # Obtiene la respuesta del asistente de ChatGPT
    reply = response['choices'][0]['message']['content']

    return reply

# Inicia el servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000)


