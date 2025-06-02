from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    message = os.environ.get('DEMO_MESSAGE', 'Hello, World!')
    mode = os.environ.get('DEMO_MODE', 'false')
    return f"<h1>{message}</h1><p>Demo mode: {mode}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
