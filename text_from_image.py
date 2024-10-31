import pytesseract
from PIL import Image
import streamlit as st

# Specify the path to the tesseract executable if it's not in your PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def text_from_image():
    st.header("Text From Image Tesseract")

    uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        # Add custom configuration for Tesseract
        # The --oem 1 option specifies the OCR Engine Mode (1 for LSTM).
        # The --psm 6 option assumes a single uniform block of text.
        custom_config = r'--oem 1 --psm 6'
        
        # Recognize text in the image
        text = pytesseract.image_to_string(image, config=custom_config)
        st.write("Extracted Text:")
        st.write(text)
