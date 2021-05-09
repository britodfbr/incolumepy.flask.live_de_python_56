from flask import jsonify, render_template, url_for


def configure(app):

    @app.route('/')
    def index():
        return render_template('index.html', title='Home')


    @app.route('/home')
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
    @app.route('/contact')
    def contact():
        return "Contato"
    #     # return render_template(
    #     #     'contact.html',
    #     #      title='Contato'
    #     # )