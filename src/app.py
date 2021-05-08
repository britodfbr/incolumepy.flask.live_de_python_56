from flask import Flask
from src import views
from src import contact


def create_app():
    app = Flask(__name__)
    views.configure(app)
    # configurar extensões
    contact.configure(app)
    # configurar variáveis
    return app
