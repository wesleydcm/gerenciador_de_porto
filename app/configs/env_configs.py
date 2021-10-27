from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()


def init_app(app:Flask):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = bool(os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS'))
    app.config['JSON_SORT_KEYS'] = bool(os.environ.get('JSON_SORT_KEYS'))
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    if os.environ.get('FLASK_ENV') == 'production':
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace('postgres', 'postgresql')
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

