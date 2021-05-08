from main import create_app

application = app = create_app()

# Start para produção
# pip install gunicorn
# gunicorn wsgi:app