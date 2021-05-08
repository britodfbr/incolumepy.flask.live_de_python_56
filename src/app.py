from flask import Flask
from src import views


def create_app():
    app = Flask(__name__)
    views.configure(app)
    # configurar extensões
    # configurar variáveis
    return app
