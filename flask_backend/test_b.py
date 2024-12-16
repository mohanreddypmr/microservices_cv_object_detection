from flask import Flask, request, jsonify, send_file
from PIL import Image, ImageFilter
import io
import os

app = Flask(__name__)

import cv2

# Temporary folder to save images
TEMP_FOLDER = "temp_images"
os.makedirs(TEMP_FOLDER, exist_ok=True)

from test import detect

@app.route('/process-image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}) , 400

    image_file = request.files['image']

    # Open the image
    try:
        img = Image.open(image_file)
    except Exception as e:
        return jsonify({"error": "Invalid image file"}) , 400

    # # Process the image (e.g., apply a blur filter)
    # processed_img = img.filter(ImageFilter.BLUR)
    img.save('input_img.jpg')
    processed_img ,txt_out = detect('input_img.jpg')
    txt_out = txt_out.replace('\n','&')
    # Save the processed image temporarily
    processed_image_path = os.path.join(TEMP_FOLDER, "processed_image.png")
    cv2.imwrite( processed_image_path , processed_img )
    #processed_img.save(processed_image_path)

    # Generate a text output (e.g., simple description)
    description = "This is a detection model output image ."

    # Send the processed image and text as response
    return send_file(
        processed_image_path,
        mimetype='image/png',
        as_attachment=False,
        #attachment_filename='processed_image.png'
    ), 200, {'X-Description': txt_out}

app.run(debug=True,port=5005)