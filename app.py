import os
import uuid
from flask import Flask, request, render_template, send_file, jsonify
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'processed')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'bmp'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file uploaded'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not supported. Use PNG, JPG, JPEG, WEBP, or BMP.'}), 400

    try:
        input_bytes = file.read()
        output_bytes = remove(input_bytes)

        if not isinstance(output_bytes, bytes):
            return jsonify({'error': 'Unexpected output format from background removal'}), 500

        # Save processed image with a unique name
        output_filename = f"{uuid.uuid4().hex}.png"
        output_path = os.path.join(UPLOAD_FOLDER, output_filename)

        img = Image.open(io.BytesIO(output_bytes)).convert("RGBA")
        img.save(output_path, format='PNG')

        return jsonify({
            'success': True,
            'filename': output_filename
        })

    except Exception as e:
        return jsonify({'error': f'Processing failed: {str(e)}'}), 500


@app.route('/download/<filename>')
def download(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(filepath):
        return jsonify({'error': 'File not found'}), 404
    return send_file(filepath, as_attachment=True, download_name='bg_removed.png')


@app.route('/preview/<filename>')
def preview(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(filepath):
        return jsonify({'error': 'File not found'}), 404
    return send_file(filepath, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)
