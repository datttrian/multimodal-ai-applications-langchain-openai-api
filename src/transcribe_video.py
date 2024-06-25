import glob
import os

import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

# Directory to store the downloaded video
output_dir = "files/audio/"

# Find all the audio files in the output directory
audio_files = glob.glob(os.path.join(output_dir, "*.mp3"))

# Select the first audio file in the list
audio_filename = audio_files[0]

# Define function parameters
audio_file = audio_filename
output_file = "files/transcripts/transcript.txt"
model = "whisper-1"

# Transcribe the audio file to text using OpenAI API
audio_file = open(audio_file, "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
)
