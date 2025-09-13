
from os import environ
from FlaskWebProject import app

if __name__ == '__main__':
    HOST = '0.0.0.0'
    PORT = int(environ.get('PORT', 8000))  # Azure expects 8000
    app.run(HOST, PORT)
