from flask import Flask
from flask_admin import Admin

from flaskblog.config import Config
from flaskblog.errors.handlers import errors
from flaskblog.main.routes import main


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
