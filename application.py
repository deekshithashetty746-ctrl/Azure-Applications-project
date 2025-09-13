from os import environ
from FlaskWebProject import app

if __name__ == '__main__':
    host = '0.0.0.0'  # Must be 0.0.0.0 for Azure
    port = int(environ.get('PORT', 5000))  # Azure automatically sets PORT
    app.run(host=host, port=port)  # Remove ssl_context
