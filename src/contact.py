from flask import Blueprint, render_template


bp = Blueprint('contact', __name__, url_prefix='/contact')


@bp.route('/')
def contact():
    # return 'Fale conosco'
    return render_template(
        'contact.html',
        title='Fale conosco'
    )


def configure(app):
    app.register_blueprint(bp)
