from flask import Flask
from application.extensions import db, ma, jwt
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    from application.blueprints.members import members_bp
    app.register_blueprint(members_bp)

    return app
