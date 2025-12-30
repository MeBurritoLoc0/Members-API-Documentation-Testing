from flask import Flask
from config import config

from application.extensions import db, ma, jwt
from application.blueprints.members.routes import members_bp
from application.blueprints.math.routes import math_bp


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    # Register blueprints (THIS IS THE KEY)
    app.register_blueprint(members_bp)
    app.register_blueprint(math_bp)

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
