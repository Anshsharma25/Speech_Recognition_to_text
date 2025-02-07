import speech_recognition as sr
from googletrans import Translator

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
        text = recognizer.recognize_google(audio, language='hi-IN')  # Assuming input is in Hindi
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

if __name__ == "__main__":
    main()
