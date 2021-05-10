from flask import Flask
from . import views
from . import contact

def create_app():
    app = Flask(__name__)
    views.configure(app)
    # configurar extensões
    contact.configure(app)
    # configurar variáveis
    return app
