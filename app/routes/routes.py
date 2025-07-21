from flask import Blueprint, request, redirect, render_template, session, current_app
from datetime import datetime
import uuid
import os
from werkzeug.utils import secure_filename
import csv

from app.models import db, Dataset  

upload_bp = Blueprint('upload_bp', __name__)


# Pastas
UPLOAD_FOLDER_VIDEO = 'app/static/uploads/videos'
os.makedirs(UPLOAD_FOLDER_VIDEO, exist_ok=True)



# Rota principal (listar)
@upload_bp.route('/')
def index():
    datasets = Dataset.query.order_by(Dataset.data_criacao.desc()).all()
    return render_template('index.html', documentos=datasets)

# Rota Fluxogramas
@upload_bp.route('/metodologia')
def fluxograma():
    return render_template('metodologia.html')


#Rota Sobre
@upload_bp.route('/sobre')
def sobre():
    return render_template('sobre.html')

#Rota webcam:
@upload_bp.route('/webcam')
def webcam():
    return render_template('webcam.html')

#Login
@upload_bp.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']
        config = current_app.config

        if username == config['USERNAME'] and password == config['PASSWORD']:
            session['logged_in'] = True
            return redirect('/')
        else:
            error = 'Usuário ou senha inválidos'

    return render_template('login.html', error=error)

#Rota de logout
@upload_bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/login')

# Criar novo tópico
@upload_bp.route('/upload', methods=['GET', 'POST'])
#@login_required
def upload():
    if request.method == 'POST':
        # Recebe os dados do formulário
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        criador = request.form['criador']
        video = request.files.get('video')

        # Gera um ID único (8 caracteres)
        id_unico = str(uuid.uuid4())[:8]

        # Define o caminho do arquivo de vídeo
        caminho_arquivo = ''
        if video and video.filename != '':
            video_filename = f'{id_unico}_{secure_filename(video.filename)}'
            video_path = os.path.join(UPLOAD_FOLDER_VIDEO, video_filename)
            video.save(video_path)
            caminho_arquivo = f'static/uploads/videos/{video_filename}'

        # Cria o objeto Dataset
        novo_dataset = Dataset(
            id=id_unico,
            nome=titulo,
            criador=criador,
            data_criacao=datetime.now(),
            descricao=descricao,
            caminho_arquivos=caminho_arquivo
        )

        # Salva no banco de dados
        db.session.add(novo_dataset)
        db.session.commit()

        return redirect('/')

    return render_template('form.html')

# Editar tópico
@upload_bp.route('/edit/<id>', methods=['GET', 'POST'])
#@login_required
def edit(id):
    doc = Dataset.query.get(id)
    if not doc:
        return "Documento não encontrado", 404

    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        video = request.files.get('video')

        doc.nome = titulo
        doc.descricao = descricao

        if video and video.filename != '':
            video_filename = f'{id}_{secure_filename(video.filename)}'
            video_path = os.path.join(UPLOAD_FOLDER_VIDEO, video_filename)
            video.save(video_path)
            doc.caminho_arquivos = f'static/uploads/videos/{video_filename}'

        db.session.commit()
        return redirect('/')

    return render_template('edit.html', documento=doc)

# Deletar tópico (soft delete)
@upload_bp.route('/delete/<id>', methods=['POST'])
#@login_required
def delete(id):
    doc = Dataset.query.get(id)
    if doc:
        doc.status = 'inativo'
        db.session.commit()
    return redirect('/')


@upload_bp.route('/restaurar/<id>', methods=['POST'])
#@login_required
def restaurar(id):
    doc = Dataset.query.get(id)
    if doc:
        doc.status = 'ativo'
        db.session.commit()
    return redirect('/excluidos')

@upload_bp.route('/excluidos')
#@login_required
def excluidos():
    inativos = Dataset.query.filter_by(status='inativo').all()
    return render_template('excluidos.html', documentos=inativos)

@upload_bp.route('/delete_permanente/<id>', methods=['POST'])
#@login_required
def delete_permanente(id):
    doc = Dataset.query.get(id)
    if doc:
        # Remove arquivo de vídeo se existir
        if doc.caminho_arquivos and os.path.exists(doc.caminho_arquivos):
            os.remove(doc.caminho_arquivos)
        db.session.delete(doc)
        db.session.commit()
    return redirect('/excluidos')