import os
from flask import Flask, request, redirect, render_template
from werkzeug.utils import secure_filename
from main import extract_text, segment_visual_elements, generate_html



# Define the allowed file extensions
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

# Initialize Flask app
app = Flask(__name__)

# Set the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to handle file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Perform processing on the uploaded image
        text = extract_text(file_path)
        image_elements = segment_visual_elements(file_path, 'static/elements')
        generate_html(text, image_elements, 'templates/result.html')

        return redirect('/result')

# Route to upload image
@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        return redirect('/upload')
    return render_template('upload.html')

# Route to display result
@app.route('/result', methods=['GET'])
def display_result():
    return render_template('result.html')

# Run the app if executed directly
if __name__ == '__main__':
    app.run(debug=True)