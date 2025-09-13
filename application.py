from FlaskWebProject import app

if __name__ == '__main__':
    host = '0.0.0.0'               # Must bind to 0.0.0.0 for Azure
    port = int(os.environ.get('PORT', 8000))  # Azure sets PORT automatically
    app.run(host=host, port=port)  # No SSL context
