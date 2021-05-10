from tinymongo import TinyMongoClient


def get_db():
    conn = TinyMongoClient()
    db = conn.mydatabase
    return db


def configure(app):
    app.db = get_db()
