from flask import Flask
from application.extensions import db, ma, jwt
from application.blueprints.math.routes import math_bp
from application.blueprints.members.routes import members_bp
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(math_bp)
    app.register_blueprint(members_bp)

    return app
