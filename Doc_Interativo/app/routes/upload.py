from flask import Blueprint, request, redirect, render_template
import os
import uuid
import csv
from werkzeug.utils import secure_filename

upload_bp = Blueprint('upload_bp', __name__)

# Pastas
CSV_PATH = 'table.csv'
UPLOAD_FOLDER_VIDEO = 'app/static/uploads/videos'
UPLOAD_FOLDER_PDF = 'app/static/uploads/pdfs'
DESCRICOES_FOLDER = 'data/descricoes'

# Garante que as pastas existem
os.makedirs(UPLOAD_FOLDER_VIDEO, exist_ok=True)
os.makedirs(UPLOAD_FOLDER_PDF, exist_ok=True)
os.makedirs(DESCRICOES_FOLDER, exist_ok=True)

# Função auxiliar para carregar os dados
def carregar_dados():
    documentos = []
    if os.path.exists(CSV_PATH):
        with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) < 5:
                    continue
                descricao_texto = ''
                if os.path.exists(row[4]):
                    with open(row[4], 'r', encoding='utf-8') as f:
                        descricao_texto = f.read()

                documentos.append({
                    'id': row[0],
                    'titulo': row[1],
                    'video': '/' + row[2].replace('app/', '') if row[2] else '',
                    'pdf': '/' + row[3].replace('app/', '') if row[3] else '',
                    'descricao': descricao_texto,
                    'desc_path': row[4],
                    'video_path': row[2],
                    'pdf_path': row[3]
                })
    return documentos

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
                doc['desc_path']
            ])

# Rota principal (listar)
@upload_bp.route('/')
def index():
    documentos = carregar_dados()
    return render_template('index.html', documentos=documentos)

# Criar novo tópico
@upload_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        video = request.files.get('video')
        pdf = request.files.get('pdf')

        id_unico = str(uuid.uuid4())[:8]

        video_path = ''
        pdf_path = ''
        desc_path = f'{DESCRICOES_FOLDER}/{id_unico}.txt'

        if video and video.filename != '':
            video_filename = f'{id_unico}_{secure_filename(video.filename)}'
            video.save(os.path.join(UPLOAD_FOLDER_VIDEO, video_filename))
            video_path = f'static/uploads/videos/{video_filename}'

        if pdf and pdf.filename != '':
            pdf_filename = f'{id_unico}_{secure_filename(pdf.filename)}'
            pdf.save(os.path.join(UPLOAD_FOLDER_PDF, pdf_filename))
            pdf_path = f'static/uploads/pdfs/{pdf_filename}'

        with open(desc_path, 'w', encoding='utf-8') as f:
            f.write(descricao)

        with open(CSV_PATH, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([id_unico, titulo, video_path, pdf_path, desc_path])

        return redirect('/')

    return render_template('form.html')

# Editar tópico
@upload_bp.route('/edit/<id>', methods=['GET', 'POST'])
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
def delete(id):
    documentos = carregar_dados()
    documentos = [doc for doc in documentos if doc['id'] != id]
    salvar_dados(documentos)
    return redirect('/')
