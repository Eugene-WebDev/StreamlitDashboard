import streamlit as st
from youtube_downloader import youtube_downloader
from mp4_to_mp3 import mp4_to_mp3
from text_from_image import text_from_image


def main():
    st.title("Dashboard")

    # Sidebar navigation
    project = st.sidebar.radio(
        "Select a Project",
        ("YouTube Downloader", "MP4 to MP3 Converter", "Extract Text from Image")
    )

    # Display selected project content
    if project == "YouTube Downloader":
        youtube_downloader()
    elif project == "MP4 to MP3 Converter":
        mp4_to_mp3()
    elif project == "Extract Text from Image":
        text_from_image()

if __name__ == "__main__":
    main()