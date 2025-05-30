from flask import Flask, request, jsonify
from flask_cors import CORS
import pytesseract
from PIL import Image, UnidentifiedImageError
import io
from pdf2image import convert_from_bytes

# ✅ Path to Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# ✅ Path to Poppler (used by pdf2image)
POPPLER_PATH = r'C:\Program Files\poppler\poppler-24.08.0\Library\bin'

app = Flask(__name__)
CORS(app)

@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    filename = file.filename.lower()

    try:
        if filename.endswith('.txt'):
            text = file.read().decode('utf-8')
            return jsonify({'success': True, 'file_type': 'txt', 'text': text})

        elif filename.endswith('.pdf'):
            print("Received a PDF file")
            images = convert_from_bytes(file.read(), poppler_path=POPPLER_PATH)
            print(f"Converted PDF to {len(images)} images")
            full_text = ""
            for i, img in enumerate(images):
                print(f"Processing page {i + 1}")
                page_text = pytesseract.image_to_string(img)
                full_text += f"\n\n--- Page {i + 1} ---\n{page_text}"
            return jsonify({'success': True, 'file_type': 'pdf', 'text': full_text})

        else:
            print("Received an image file")
            img_bytes = file.read()
            img = Image.open(io.BytesIO(img_bytes))
            text = pytesseract.image_to_string(img)
            return jsonify({'success': True, 'file_type': 'image', 'text': text})

    except UnidentifiedImageError:
        print("UnidentifiedImageError: invalid image or PDF")
        return jsonify({'error': 'Uploaded file is not a valid image or PDF'}), 400

    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

@app.route('/')
def index():
    return 'Flask backend is running!'

if __name__ == '__main__':
    app.run(debug=True)
