from flask import Flask
from flask_cors import CORS
from .config import Config

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object(Config)
    CORS(app)

    # Importa e registra as rotas
    from app.routes.upload import upload_bp
    app.register_blueprint(upload_bp)

    return app
