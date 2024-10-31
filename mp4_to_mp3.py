import os
from pydub import AudioSegment
import streamlit as st

# Define the directory to store downloads
DOWNLOAD_DIR = "downloads"

# Ensure download directory exists
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

def mp4_to_mp3():
    st.header("MP4 to MP3 Converter")

    # Step 1: File upload for MP4
    uploaded_file = st.file_uploader("Upload MP4 file", type=["mp4"])

    # Step 2: Convert button
    if uploaded_file is not None and st.button("Convert to MP3"):
        # Save the uploaded MP4 file into the downloads directory
        mp4_file_path = os.path.join(DOWNLOAD_DIR, uploaded_file.name)
        
        try:
            with open(mp4_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())  # Use getbuffer() to read the BytesIO object

            # Define output path for MP3
            mp3_file_path = os.path.join(DOWNLOAD_DIR, os.path.splitext(uploaded_file.name)[0] + ".mp3")

            # Convert MP4 to MP3 using pydub
            audio = AudioSegment.from_file(mp4_file_path, format="mp4")
            audio.export(mp3_file_path, format="mp3")

            st.success("Conversion successful!")
            st.write("Click the link below to download your MP3 file.")

            # Provide download link for the MP3 file
            with open(mp3_file_path, "rb") as file:
                st.download_button(
                    label="Download MP3",
                    data=file,
                    file_name=os.path.basename(mp3_file_path),
                    mime="audio/mp3"
                )

        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.write("Debug Information:")
            st.write(f"MP4 file path: {mp4_file_path}")
            st.write(f"MP3 file path: {mp3_file_path}")
