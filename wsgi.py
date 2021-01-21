from app import create_app
from os import environ

application = create_app(environ.get('FLASK_ENV'))

if __name__ == "__main__":
    application.run()
