import streamlit as st
from PIL import Image, ImageOps
import io

import requests
url = "http://127.0.0.1:5005/process-image"


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
    original_image.save('in_put.jpg')
    # Image file to send
    image_path = 'in_put.jpg'
    print(image_path,type(image_path))
    with open(image_path, "rb") as image_file:
        files = {"image": image_file}
        response = requests.post(url, files=files)

    # Check response
    if response.status_code == 200:
        # Save the processed image
        with open("processed_image.png", "wb") as f:
            f.write(response.content)
        
        # Retrieve description from response headers
        description = response.headers.get("X-Description", "No description provided.")
        print("Description:", description)
    else:
        print(response.status_code)
        try:
            # If server returns JSON error, parse it
            print("Error:", response.json())
        except Exception as e:
            # Handle non-JSON errors
            print("Error: Could not parse server response.")

    st.image(original_image, caption="Uploaded Image",)

    # Process the image
    st.subheader("Processed Image")
    processed_image = "processed_image.png" 
    st.image(processed_image, caption="Processed Image",)

    # Save processed image to BytesIO
    # processed_image_buffer = io.BytesIO()
    # processed_image.save(processed_image_buffer, format="PNG")
    # processed_image_buffer.seek(0)

    # # Display download button for processed image
    # st.download_button(
    #     label="Download Processed Image",
    #     data=processed_image_buffer,
    #     file_name="processed_image.png",
    #     mime="image/png"
    # )

    # Example textual output (you can replace this with your model's text output)
    st.subheader("Textual Output")
    text_output = "This is an example description of the uploaded image."
    st.text_area("Generated Text", description.replace('&','\n'), height=100)


