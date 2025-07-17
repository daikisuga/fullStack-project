from flask import Flask, request, render_template, jsonify
# cv2 = OpenCV, base64 = Decodifica a imagem (vem como string base64 do navegador), os = Cria diretórios, re = remove o cabeçalho base64 da string da imagem
import cv2, base64, os, re
import numpy as np

app = Flask(__name__)
# Serve para mapear as imagens, por exemplo: frame_0.jpg, frame_1.jpg,...
count = 0

# Ao acessar o site a rota responde
@app.route('/')
def index():
    # webcam.html precisa estar em estrutura.txt
    return render_template('webcam.html')

@app.route('/upload_frame', methods=['POST'])
def upload_frame():
    
    global count

    # Faz a leitura da requisição json
    data = request.get_json()

    # Retorna um erro quando a captura falhar. "Image" é uma chave que vem com cada imagem
    if 'image' not in data:
        return jsonify({'error': 'Imagem não enviada!'}), 400
    
    # Remove o cabeçalho base64 da imagem
    img_data = re.sub('^data:image/.+;base64,', '', data['image'])

    # Converte a imagem para o OpenCV
    img_bytes = base64.b64decode(img_data) # Necessário converter para bytes binários
    img_array = np.frombuffer(img_bytes, np.uint8) # Transforma os bytes em um array de Numpy
    frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR) # Converte o array em uma imagem OpenCV

    # Cria o diretório
    os.makedirs("frames", exist_ok=True)
    # Nomeia a imagem (usa o count para ser sequencial)
    file_name = f"frames/frame_{count}.jpg"
    # Salva o frame como jpg
    cv2.imwrite(file_name, frame)
    count += 1

    # Manda uma mensagem de sucesso
    return jsonify({'status': 'Frame recebido!'})

if __name__ == '__main__':
    app.run(debug=True)
