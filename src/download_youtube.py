import glob
import os

import yt_dlp as youtube_dl
from yt_dlp import DownloadError

# An example YouTube tutorial video
youtube_url = "https://www.youtube.com/watch?v=aqzxYofJ_ck"

# Directory to store the downloaded video
output_dir = "files/audio/"

# Config for youtube-dl
ydl_config = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
    "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
    "verbose": True,
}

# Check if the output directory exists, if not create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Print a message indicating which video is being downloaded
print(f"Downloading video from {youtube_url}")

# Attempt to download the video using the specified configuration
# If a DownloadError occurs, attempt to download the video again
try:
    with youtube_dl.YoutubeDL(ydl_config) as ydl:
        ydl.download([youtube_url])
except DownloadError:
    with youtube_dl.YoutubeDL(ydl_config) as ydl:
        ydl.download([youtube_url])

# Find all the audio files in the output directory
audio_files = glob.glob(os.path.join(output_dir, "*.mp3"))

# Select the first audio file in the list
audio_filename = audio_files[0]

# Print the name of the selected audio file
print(audio_filename)
