import os
import io
import cv2
from google.cloud import vision
from PIL import Image, ImageDraw

# Set the environment variable for Google Application Credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'citric-earth-424205-p9-7a89655bb49a.json'

def extract_text(image_path):
    client = vision.ImageAnnotatorClient()
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        return texts[0].description
    return ''

def segment_visual_elements(image_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    image_elements = []
    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        if w > 50 and h > 50:  # Filter out small elements
            roi = image[y:y+h, x:x+w]
            element_path = os.path.join(output_dir, f'element_{i}.png')
            cv2.imwrite(element_path, roi)
            image_elements.append(element_path)
    
    return image_elements

def generate_html(text, image_elements, output_html):
    html_content = '<html><body>\n'
    
    if text:
        paragraphs = text.split('\n')
        for para in paragraphs:
            html_content += f'<p>{para}</p>\n'
    
    for i, img_path in enumerate(image_elements):
        html_content += f'<img src="{img_path}" alt="Visual Element {i}">\n'
    
    html_content += '</body></html>'
    
    with open(output_html, 'w', encoding='utf-8') as file:
        file.write(html_content)