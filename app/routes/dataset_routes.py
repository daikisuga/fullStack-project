from flask import Blueprint, request, redirect, render_template
from datetime import datetime
import uuid
import os

from app.models import db, Dataset
from .video_files import salvar_video

dataset_bp = Blueprint('dataset_bp', __name__)

@dataset_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        id_unico = str(uuid.uuid4())[:8]
        caminho = salvar_video(request.files.get('video'), id_unico)

        novo_dataset = Dataset(
            id=id_unico,
            nome=request.form['titulo'],
            criador=request.form['criador'],
            data_criacao=datetime.now(),
            descricao=request.form['descricao'],
            caminho_arquivos=caminho
        )
        db.session.add(novo_dataset)
        db.session.commit()
        return redirect('/')
    return render_template('form.html')

@dataset_bp.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    doc = Dataset.query.get(id)
    if not doc:
        return "Documento não encontrado", 404

    if request.method == 'POST':
        doc.nome = request.form['titulo']
        doc.descricao = request.form['descricao']
        video = request.files.get('video')

        if video and video.filename != '':
            doc.caminho_arquivos = salvar_video(video, id)
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', documento=doc)

@dataset_bp.route('/delete/<id>', methods=['POST'])
def delete(id):
    doc = Dataset.query.get(id)
    if doc:
        doc.status = False
        db.session.commit()
    return redirect('/')

@dataset_bp.route('/restaurar/<id>', methods=['POST'])
def restaurar(id):
    doc = Dataset.query.get(id)
    if doc:
        doc.status = True
        db.session.commit()
    return redirect('/excluidos')

@dataset_bp.route('/excluidos')
def excluidos():
    inativos = Dataset.query.filter_by(status=False).all()
    return render_template('excluidos.html', documentos=inativos)

@dataset_bp.route('/delete_permanente/<id>', methods=['POST'])
def delete_permanente(id):
    doc = Dataset.query.get(id)
    if doc:
        if doc.caminho_arquivos and os.path.exists(doc.caminho_arquivos):
            os.remove(doc.caminho_arquivos)
        db.session.delete(doc)
        db.session.commit()
    return redirect('/excluidos')
