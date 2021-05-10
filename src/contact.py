from flask import Blueprint, render_template, request


bp = Blueprint('contact', __name__, url_prefix='/contact')


@bp.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        # return 'Fale conosco'
        return render_template(
            'contact.html',
            title='Fale conosco'
        )
    # TODO processar dados
    print(request.form)
    return "Tua mensagem foi enviada com sucesso!"

def configure(app):
    app.register_blueprint(bp)
