# Importing the Required Packages including: "os" "openai" "yt_dlp as
# youtube_dl" and "from yt_dl import Download Error"

# Import the os package
import os

# Import the glob package
import glob

# Import the openai package
import openai

# Import the yt_dlp package as youtube_dl
import yt_dlp as youtube_dl

# Import DownloadError from yt_dlp
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
    "verbose": True
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


# Find the audio file in the output directory

# Find all the audio files in the output directory
audio_files = glob.glob(os.path.join(output_dir, "*.mp3"))


# Select the first audio file in the list
audio_filename = audio_files[0]

# Print the name of the selected audio file
print(audio_filename)

# Define function parameters
audio_file = audio_filename
output_file = "files/transcripts/transcript.txt"
model = "whisper-1"

# Print the name of the audio file
print(audio_file)


# Transcribe the audio file to text using OpenAI API
print("converting audio to text...")

with open(audio_file, "rb") as audio:
    response = openai.Audio.transcribe(model, audio)

# Extract the transcript from the response
transcript = (response["text"])
