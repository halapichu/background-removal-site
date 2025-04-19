from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            input_image = Image.open(file.stream).convert("RGBA")
            output = remove(input_image)
            byte_io = io.BytesIO()
            output.save(byte_io, 'PNG')
            byte_io.seek(0)
            return send_file(byte_io, mimetype='image/png', as_attachment=True, download_name='no-bg.png')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
