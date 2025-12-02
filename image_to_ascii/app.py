from flask import Flask, request, send_file, render_template
from PIL import Image
import io
import os

app = Flask(__name__)

# Caracteres ASCII para conversão (do mais claro para o mais escuro)
ASCII_CHARS = '@%#*+=-:. '

def convert_image_to_ascii(image, cols=100, scale=0.5):
    """
    Converte uma imagem PIL para arte ASCII.
    """
    # Converte para escala de cinza
    image = image.convert("L")

    # Redimensiona a imagem
    width, height = image.size
    new_width = cols
    new_height = int(new_width * height / width * scale)
    image = image.resize((new_width, new_height))

    # Pega os pixels e mapeia para caracteres ASCII
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel * (len(ASCII_CHARS)-1) // 255] for pixel in pixels])

    # Formata a string ASCII em linhas
    ascii_art = []
    for i in range(0, len(ascii_str), new_width):
        ascii_art.append(ascii_str[i:i+new_width])
    return "\n".join(ascii_art)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return render_template('index.html', error='Nenhum arquivo enviado')

    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', error='Nenhum arquivo selecionado')

    if file:
        try:
            image = Image.open(io.BytesIO(file.read()))
            ascii_art = convert_image_to_ascii(image)

            if request.form.get('download_txt'):
                # Retorna como arquivo .txt para download
                mem_file = io.BytesIO()
                mem_file.write(ascii_art.encode('utf-8'))
                mem_file.seek(0)
                return send_file(
                    mem_file,
                    mimetype='text/plain',
                    as_attachment=True,
                    download_name='ascii_art.txt'
                )
            else:
                # Retorna a arte ASCII para o template
                return render_template('index.html', ascii_art=ascii_art)
        except Exception as e:
            return render_template('index.html', error=f'Erro ao processar a imagem: {e}')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
