import os
from yt_dlp import YoutubeDL
import streamlit as st

# Define a directory to store downloads
DOWNLOAD_DIR = "downloads"

def youtube_downloader():
    st.header("YouTube Video Downloader")

    # Ensure the download directory exists
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

    # Step 1: Input field for the YouTube URL
    url = st.text_input("Enter YouTube video URL (e.g., https://www.youtube.com/watch?v=XXXX):")

    # Step 2: Download button
    if st.button("Download"):
        if url and (url.startswith("https://www.youtube.com/") or url.startswith("https://youtu.be/")):
            # Define primary video download options
            ydl_opts_video = {
                'format': 'bestvideo+bestaudio',  # Try to get best video and audio
                'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
                'noplaylist': True,
            }

            # Define fallback audio-only download options
            ydl_opts_audio = {
                'format': 'bestaudio',
                'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
                'noplaylist': True,
            }

            try:
                # Attempt to download video
                with YoutubeDL(ydl_opts_video) as ydl:
                    info = ydl.extract_info(url, download=True)
                    video_title = info.get('title', 'video')
                    video_path = os.path.join(DOWNLOAD_DIR, f"{video_title}.mp4")
                    st.success(f"Downloaded Video: {video_title}")
                    
            except Exception as e:
                st.warning(f"Video download failed: {e}. Attempting audio-only download...")
                # Attempt to download audio only if video fails
                try:
                    with YoutubeDL(ydl_opts_audio) as ydl:
                        info = ydl.extract_info(url, download=True)
                        audio_title = info.get('title', 'audio')
                        audio_path = os.path.join(DOWNLOAD_DIR, f"{audio_title}.mp3")
                        st.success(f"Downloaded Audio: {audio_title}")
                        video_path = audio_path  # Update path to provide download link
                    
                except Exception as audio_error:
                    st.error(f"Audio download failed as well: {audio_error}")
                    return

            # Provide download link
            if os.path.exists(video_path):
                with open(video_path, "rb") as file:
                    st.download_button(
                        label="Download File",
                        data=file,
                        file_name=os.path.basename(video_path),
                        mime="video/mp4" if video_path.endswith(".mp4") else "audio/mp3"
                    )
            else:
                st.error("Download path does not exist.")

        else:
            st.error("Please enter a valid YouTube URL.")
