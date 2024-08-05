import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = '7411955725:AAHtfKrRw--H0DSjL1_HfOl14_wVh7F02ow'
URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
MINI_APP_URL = 'https://dlutsok.github.io/telegram-mini-app/'

@app.route('/send_message', methods=['POST'])
def send_message():
    chat_id = request.json.get('chat_id')
    data = {
        'chat_id': chat_id,
        'text': 'Click the button below to open the presentation:',
        'reply_markup': {
            'inline_keyboard': [[{
                'text': 'Open Presentation',
                'url': MINI_APP_URL
            }]]
        }
    }
    response = requests.post(URL, json=data)
    return {'status': 'ok'} if response.status_code == 200 else {'status': 'failed'}

if __name__ == '__main__':
    app.run(port=5001)
