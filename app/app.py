from flask import Flask
import config


def create_app():
    app = Flask(
        __name__,
        template_folder=config.template_folder,
        static_folder=config.static_folder,
    )
    app.config["SECRET_KEY"] = 'secret'

    from app import views

    views.init_app(app)

    return app
