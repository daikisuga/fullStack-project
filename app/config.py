import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    UPLOAD_FOLDER = os.path.join(BASE_DIR, '..', 'uploads')
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/hub_datasets'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'sua-chave-secreta'