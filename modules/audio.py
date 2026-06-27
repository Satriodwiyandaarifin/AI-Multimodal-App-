from gtts import gTTS
import os

def generate_audio(text):
    tts = gTTS(text=text, lang='id')  # bisa ganti 'en' kalau mau Inggris
    
    file_path = "output.mp3"
    tts.save(file_path)
    
    return file_path