"""
The flask application package.
"""
import logging
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

# ===== Logging Configuration =====
# Log to a file
if not os.path.exists('logs'):
    os.mkdir('logs')
file_handler = logging.FileHandler('logs/app.log')
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s [in %(pathname)s:%(lineno)d]'
)
file_handler.setFormatter(file_formatter)
app.logger.addHandler(file_handler)

# Log to console (for Azure Log Stream)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'
)
console_handler.setFormatter(console_formatter)
app.logger.addHandler(console_handler)

# Set overall logger level
app.logger.setLevel(logging.INFO)
app.logger.info('FlaskWebProject startup')

# ===== Flask Extensions =====
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

# ===== Import views =====
import FlaskWebProject.views
