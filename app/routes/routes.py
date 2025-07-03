from flask import Blueprint, request, redirect, render_template, session, current_app
from datetime import datetime
import uuid
import os
from werkzeug.utils import secure_filename
import csv

from app.models import db, Dataset  

upload_bp = Blueprint('upload_bp', __name__)

# Pastas
CSV_PATH = 'table.csv'
UPLOAD_FOLDER_VIDEO = 'app/static/uploads/videos'
UPLOAD_FOLDER_PDF = 'app/static/uploads/pdfs'
DESCRICOES_FOLDER = 'data/desc_documentacao'

# Garante que as pastas existem
os.makedirs(UPLOAD_FOLDER_VIDEO, exist_ok=True)
os.makedirs(UPLOAD_FOLDER_PDF, exist_ok=True)
os.makedirs(DESCRICOES_FOLDER, exist_ok=True)

# Função auxiliar para carregar os dados
def carregar_dados():
    dados = []
    if os.path.exists(CSV_PATH):
        with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) < 5:
                    continue

                desc_texto = ''
                
                if os.path.exists(row[4]):
                    with open(row[4], 'r', encoding='utf-8') as f:
                        desc_texto = f.read()

                # Pega o status, se não tiver (linha antiga), assume 'ativo'
                status = row[5] if len(row) >= 6 else 'ativo'
                dados.append({
                    'id': row[0],
                    'titulo': row[1],
                    'video': '/' + row[2].replace('app/', '') if row[2] else '',
                    'pdf': '/' + row[3].replace('app/', '') if row[3] else '',
                    'descricao': desc_texto,
                    'desc_path': row[4],
                    'video_path': row[2],
                    'pdf_path': row[3],
                    'status' : status
                })
    return dados

# Função auxiliar para salvar os dados
def salvar_dados(documentos):
    with open(CSV_PATH, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for doc in documentos:
            writer.writerow([
                doc['id'],
                doc['titulo'],
                doc['video_path'],
                doc['pdf_path'],
                doc['desc_path'],
                doc['status']
            ])



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
    documentos = carregar_dados()
    doc = next((item for item in documentos if item['id'] == id), None)

    if not doc:
        return "Documento não encontrado", 404

    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        video = request.files.get('video')
        pdf = request.files.get('pdf')

        doc['titulo'] = titulo

        with open(doc['desc_path'], 'w', encoding='utf-8') as f:
            f.write(descricao)
        doc['descricao'] = descricao

        if video and video.filename != '':
            video_filename = f'{id}_{secure_filename(video.filename)}'
            video.save(os.path.join(UPLOAD_FOLDER_VIDEO, video_filename))
            doc['video_path'] = f'static/uploads/videos/{video_filename}'
            doc['video'] = '/' + doc['video_path'].replace('app/', '')

        if pdf and pdf.filename != '':
            pdf_filename = f'{id}_{secure_filename(pdf.filename)}'
            pdf.save(os.path.join(UPLOAD_FOLDER_PDF, pdf_filename))
            doc['pdf_path'] = f'static/uploads/pdfs/{pdf_filename}'
            doc['pdf'] = '/' + doc['pdf_path'].replace('app/', '')

        salvar_dados(documentos)

        return redirect('/')

    return render_template('edit.html', documento=doc)

# Deletar tópico
@upload_bp.route('/delete/<id>', methods=['POST'])
#@login_required
def delete(id):
    documentos = carregar_dados()
    for doc in documentos:
        if doc['id'] == id:
            doc['status'] = 'inativo'
            break
    salvar_dados(documentos)
    return redirect('/')


@upload_bp.route('/restaurar/<id>', methods=['POST'])
#@login_required
def restaurar(id):
    documentos = carregar_dados()
    for doc in documentos:
        if doc['id'] == id:
            doc['status'] = 'ativo'
            break
    salvar_dados(documentos)
    return redirect('/excluidos')

@upload_bp.route('/excluidos')
#@login_required
def excluidos():
    documentos = carregar_dados()
    inativos = [doc for doc in documentos if doc['status'] == 'inativo']
    return render_template('excluidos.html', documentos=inativos)

@upload_bp.route('/delete_permanente/<id>', methods=['POST'])
#@login_required
def delete_permanente(id):
    documentos = carregar_dados()
    documentos_novos = []

    for doc in documentos:
        if doc['id'] == id:
            if doc['video_path'] and os.path.exists(doc['video_path']):
                os.remove(doc['video_path'])
            if doc['pdf_path'] and os.path.exists(doc['pdf_path']):
                os.remove(doc['pdf_path'])
            if doc['desc_path'] and os.path.exists(doc['desc_path']):
                os.remove(doc['desc_path'])
        else:
            documentos_novos.append(doc)

    salvar_dados(documentos_novos)
    return redirect('/excluidos')