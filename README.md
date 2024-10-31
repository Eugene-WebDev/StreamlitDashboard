# Streamlit Dashboard Project

This project is a Streamlit-based dashboard that provides three main functionalities:
1. YouTube Video Downloader
2. MP4 to MP3 Converter
3. Text Extraction from Images using Tesseract

## Prerequisites

- Python 3.7 or higher
- Streamlit
- yt-dlp
- pydub
- pytesseract
- PIL (Pillow)
- ffmpeg (for pydub)
- Tesseract OCR


## Features

### 1. YouTube Video Downloader

- **Description**: Allows users to download videos from YouTube by providing a URL.
- **Usage**:
  - Enter a valid YouTube URL.
  - Click the "Download" button.
  - The video will be downloaded in the best available quality. If video download fails, it will attempt to download audio only.

### 2. MP4 to MP3 Converter

- **Description**: Converts uploaded MP4 video files to MP3 audio files.
- **Usage**:
  - Upload an MP4 file.
  - Click the "Convert to MP3" button.
  - The MP3 file will be available for download.

### 3. Text Extraction from Images

- **Description**: Extracts text from uploaded images using Tesseract OCR.
- **Usage**:
  - Upload an image file (PNG, JPG, JPEG).
  - The extracted text will be displayed on the screen.
 
