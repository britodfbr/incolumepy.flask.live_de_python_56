from flask import Flask
from . import views
from . import contact
from . import db

def create_app(*args, **kwargs):
    app = Flask(__name__)
    # configurar extensões
    db.configure(app)
    views.configure(app)
    contact.configure(app)
    # configurar variáveis
    app.config['SECRET_KEY'] = 'chave aleatoria'
    return app
