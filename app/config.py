import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    UPLOAD_FOLDER = os.path.join(BASE_DIR, '..', 'uploads')
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root@localhost/dataset_tcc_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'sua-chave-secreta'