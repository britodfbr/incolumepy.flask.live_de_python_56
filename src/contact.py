from flask import Blueprint, render_template, request, abort


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
    name = request.form.get('name')
    message = request.form.get('message')
    if not name or not message:
        abort(400, 'Mensagem inválida!')
    return "Tua mensagem foi enviada com sucesso!"

def configure(app):
    app.register_blueprint(bp)
