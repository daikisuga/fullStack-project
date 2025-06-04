import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    UPLOAD_FOLDER = os.path.join(BASE_DIR, '..', 'uploads')
    DEBUG = True
    SECRET_KEY = 'INFORMATICA@CMti'
    USERNAME = 'INFORMATICA'
    PASSWORD = '@teste'
