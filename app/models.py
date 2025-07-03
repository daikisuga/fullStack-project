# app/models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Dataset(db.Model):
    __tablename__ = 'datasets'

    id = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    criador = db.Column(db.String(100), nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    descricao = db.Column(db.Text)
    caminho_arquivos = db.Column(db.Text, nullable=False)
