from .main_routes import main_bp
from .auth_routes import auth_bp
#from .dataset_routes import upload_bp  # você pode renomear como dataset_bp para clareza

all_blueprints = [main_bp, auth_bp]
