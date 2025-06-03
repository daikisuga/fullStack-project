from flask import Blueprint, request, redirect, render_template
import os
import uuid
import csv

upload_bp = Blueprint('upload_bp', __name__)

UPLOAD_FOLDER_VIDEO = 'app/static/uploads/videos'
UPLOAD_FOLDER_PDF = 'app/static/uploads/pdfs'
DESCRICOES_FOLDER = 'data/descricoes'
CSV_PATH = 'table.csv'

@upload_bp.route('/')
def index():
    documentos = []
    if os.path.exists(CSV_PATH):
        with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) < 5:
                    continue
                doc = {
                    'id': row[0],
                    'titulo': row[1],
                    'video': '/' + row[2],
                    'pdf': '/' + row[3],
                    'descricao': '/' + row[4],
                }
                documentos.append(doc)
    return render_template('index.html', documentos=documentos)

@upload_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        video = request.files.get('video')
        pdf = request.files.get('pdf')

        id_unico = str(uuid.uuid4())[:8]  # Ex: 9f3a1b2c

        video_path = ''
        pdf_path = ''
        desc_path = f'{DESCRICOES_FOLDER}/{id_unico}.txt'

        if video:
            video_path = f'{UPLOAD_FOLDER_VIDEO}/{id_unico}_{video.filename}'
            video.save(video_path)

        if pdf:
            pdf_path = f'{UPLOAD_FOLDER_PDF}/{id_unico}_{pdf.filename}'
            pdf.save(pdf_path)

        with open(desc_path, 'w', encoding='utf-8') as f:
            f.write(descricao)

        with open(CSV_PATH, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([id_unico, titulo, video_path, pdf_path, desc_path])

        return redirect('/')

    return render_template('form.html')
