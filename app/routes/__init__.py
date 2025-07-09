from .main_routes import main_bp
from .auth_routes import auth_bp
from .dataset_routes import upload_bp

all_blueprints = [main_bp, auth_bp, upload_bp]
