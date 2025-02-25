from gtts import gTTS
import os

def text_to_audio(text, filename="Non-Biodegradable.mp3"):
    tts = gTTS(text=text, lang="en")
    tts.save(filename)
    os.system(f"start {filename}")  # For Windows; use `afplay` on Mac, `mpg321` on Linux

text = "Your Non-Biodegradable Waste Bin is full. Please empty it."
text_to_audio(text)
