import os
import uuid
from werkzeug.utils import secure_filename

UPLOAD_FOLDER_VIDEO = 'app/static/uploads/videos'
os.makedirs(UPLOAD_FOLDER_VIDEO, exist_ok=True)

def salvar_video(video_file, id_unico):
    if video_file and video_file.filename != '':
        filename = f'{id_unico}_{secure_filename(video_file.filename)}'
        path = os.path.join(UPLOAD_FOLDER_VIDEO, filename)
        video_file.save(path)
        return f'static/uploads/videos/{filename}'
    return ''
