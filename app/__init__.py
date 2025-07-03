from flask import Flask
from flask_cors import CORS
from app.models import db
from app.config import Config
from app.routes import all_blueprints

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object(Config)
    CORS(app)

    db.init_app(app)

    # Registro de blueprints
    for bp in all_blueprints:
        app.register_blueprint(bp)

    with app.app_context():
        db.create_all()

    return app
