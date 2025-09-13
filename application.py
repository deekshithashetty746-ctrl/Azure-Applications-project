"""
This script runs the FlaskWebProject application using a development server.
"""

from os import environ
from FlaskWebProject import app

if __name__ == '__main__':
    host = '0.0.0.0'  # Azure requires 0.0.0.0
    port = int(environ.get('PORT', 5000))  # Azure sets PORT automatically
    app.run(host=host, port=port)  # No SSL context needed; Azure handles HTTPS
