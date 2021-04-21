from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return('''
    <h1>Live de Python #56</h1>
    <br />
    <p>Desenvolvimento web com Python e Flask</p>
    <p>Bruno Rocha</p>
    ''')