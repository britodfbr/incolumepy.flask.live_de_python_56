from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return('''
    <h1>Live de Python #56</h1>
    <br />
    <p>Desenvolvimento web com Python e Flask</p>
    <p>Bruno Rocha</p>
    ''')

@app.route('/hello')
def hello():
    return "Hello live Python"


@app.route('/api')
def api_demo():
    return jsonify(data={'Key': 'Value'})