from flask import Flask
from application.extensions import db, ma, jwt
from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    # Only load Swagger when NOT testing
    if not app.config.get("TESTING"):
        from flask_swagger_ui import get_swaggerui_blueprint

        swaggerui_blueprint = get_swaggerui_blueprint(
            "/swagger",
            "/static/swagger.yaml",
            config={"app_name": "My API"}
        )

        app.register_blueprint(swaggerui_blueprint, url_prefix="/swagger")

    return app
