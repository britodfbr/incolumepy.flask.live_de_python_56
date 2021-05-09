from flask import jsonify, render_template, url_for
from io import StringIO

def configure(app):

    @app.route('/')
    def index():
        return render_template('index.html', title='Home')


    @app.route('/home')
    def home():
        return  render_template('apresentation.html', title='Apresentação')


    @app.route('/hello')
    def hello():
        return "Hello live Python"


    @app.route('/api')
    def api_demo():
        return jsonify(data={'Key': 'Value'})


    @app.route('/langs')
    def langs():
        languages = [
            'Python',
            'Java',
            'C',
            'C++',
            'JavaScript',
            'R',
            'Arduino',
            'Go',
            'Swift',
            'Matlab']
        return render_template(
            'langs.html',
            title = 'Melhores Linguagens de Programação de 2020',
            languages = languages
        )
