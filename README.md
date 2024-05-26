Image Processing Project

This project extracts and separates text and visual elements from images using Google Cloud Vision API for OCR and OpenCV for image processing. It generates an HTML file to display the separated elements. A simple Flask web interface is also provided to upload images and view results online.

Table of Contents
Technologies Used
Installation
Setup Google Cloud Vision API
Usage
Optional: Flask Web Interface
File Structure
Contributing
License
Technologies Used
Python
Google Cloud Vision API
OpenCV
Pillow
Flask

Installation
Clone the repository:
git clone https://github.com/your-username/image_processing_project.git
cd image_processing_project
Create and activate a virtual environment:

On Windows:
venv\Scripts\activate

Install required libraries:

pip install -r requirements.txt
Setup Google Cloud Vision API
Create a project on the Google Cloud Platform:

Visit the Google Cloud Console.
Create a new project or select an existing one.
Enable the Vision API:

Go to APIs & Services -> Library.
Search for Vision API and enable it.
Set up authentication:

Go to APIs & Services -> Credentials.
Create a service account key, download the JSON file, and save it in your project directory.
Set the environment variable for Google Cloud Vision API credentials:

On Windows:
set GOOGLE_APPLICATION_CREDENTIALS=path_to_your_credentials.json
Usage
Run the main script:

Place your input image in the project directory and update the image_path variable in the main.py script.
Run the script:


python main.py
Check the generated HTML file:

The script will output the path to the generated HTML file (e.g., output.html). Open this HTML file in a web browser to view the results.
Optional: Flask Web Interface
Set up Flask app:

Create a directory named uploads in your project directory.
Run the Flask app:
ba
Edit
Run
Full Screen
Copy code
python app.py
Upload an image:

Open a web browser and navigate to http://127.0.0.1:5000/. Upload an image and see the results.

File Structure
image_processing_project/
venv/
output_elements/
element_0.png
element_1.png
...
templates/
upload.html
result.html
uploads/
app.py
main.py
requirements.txt
path_to_your_credentials.json
Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request for any enhancements or new features you would like to add.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

