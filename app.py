from flask import Flask, request, jsonify
from flask import send_from_directory
app = Flask(__name__)

import os

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_image():
    print(request.files)
    if 'image' not in request.files:
        return jsonify({"error": "No file part"})

    file = request.files['image']

    if file.filename == '':
        return jsonify({"error": "No selected file"})

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return jsonify({"message": "File uploaded successfully"})
    
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
