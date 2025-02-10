import speech_recognition as sr
from googletrans import Translator
import pyttsx3

def capture_speech(recognizer, microphone):
    """
    Capture speech from the microphone and return the transcribed text.
    """
    with microphone as source:
        print("Listening... Please speak.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)  # Auto-detect language
        print(f"Recognized Text: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError:
        print("Could not request results; check your internet connection.")
        return None

def translate_text(text, target_language='en'):
    """
    Translate the given text into the target language.
    """
    translator = Translator()
    try:
        translated = translator.translate(text, dest=target_language)
        print(f"Translated Text: {translated.text}")
        return translated.text
    except Exception as e:
        print(f"Translation error: {e}")
        return None

def text_to_speech(text, language='en'):
    """
    Convert the given text to speech and play it without saving to a file.
    """
    try:
        engine = pyttsx3.init()
        engine.setProperty('voice', language)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Text-to-Speech error: {e}")

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Step 1: Capture and transcribe speech
    original_text = capture_speech(recognizer, microphone)
    if not original_text:
        return

    # Step 2: Translate the transcribed text to the target language
    target_language = 'en'  # Set the desired target language code (e.g., 'en' for English)
    translated_text = translate_text(original_text, target_language=target_language)
    if not translated_text:
        return

    # Step 3: Convert the translated text to speech
    text_to_speech(translated_text, language=target_language)

if __name__ == "__main__":
    main()