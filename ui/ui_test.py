import streamlit as st
from PIL import Image, ImageOps
import io
import numpy as np

# Title of the app
st.title("Image Upload and Processing App")

# Sidebar description
st.sidebar.title("Options")
st.sidebar.write("Upload an image to process and view the results.")

# Function to process the image (example: convert to grayscale)
def process_image(image):
    grayscale_image = ImageOps.grayscale(image)
    return grayscale_image

# Upload an image
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the original image
    st.subheader("Original Image")
    original_image = Image.open(uploaded_file)
    st.image(original_image, caption="Uploaded Image", use_column_width=True)

    # Process the image
    st.subheader("Processed Image")
    processed_image = process_image(original_image)
    st.image(processed_image, caption="Processed Image", use_column_width=True)

    # Save processed image to BytesIO
    processed_image_buffer = io.BytesIO()
    processed_image.save(processed_image_buffer, format="PNG")
    processed_image_buffer.seek(0)

    # Display download button for processed image
    st.download_button(
        label="Download Processed Image",
        data=processed_image_buffer,
        file_name="processed_image.png",
        mime="image/png"
    )

    # Example textual output (you can replace this with your model's text output)
    st.subheader("Textual Output")
    text_output = "This is an example description of the uploaded image."
    st.text_area("Generated Text", text_output, height=100)
