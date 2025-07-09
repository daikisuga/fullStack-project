from flask import Blueprint, render_template
from app.models import Dataset

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    datasets = Dataset.query.order_by(Dataset.data_criacao.desc()).all()
    return render_template('index.html', documentos=datasets)

@main_bp.route('/metodologia')
def metodologia():
    return render_template('metodologia.html')

@main_bp.route('/sobre')
def sobre():
    return render_template('sobre.html')

@main_bp.route('/webcam')
def webcam():
    return render_template('webcam.html')
