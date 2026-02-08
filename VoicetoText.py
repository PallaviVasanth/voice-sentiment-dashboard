import speech_recognition as sr

def record_and_transcribe():
    """
    Records audio from the microphone and converts it to text using SpeechRecognition.
    Returns the transcribed text or an error message if issues occur.
    """
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
            print("Listening... Speak now!")
            audio = recognizer.listen(source, timeout=5)  # Listen for up to 5 seconds
            
            # Convert speech to text using Google's API
            text = recognizer.recognize_google(audio)
            return text
    except sr.WaitTimeoutError:
        return "No speech detected. Please try again."
    except sr.UnknownValueError:
        return "Could not understand the audio. Please speak clearly."
    except sr.RequestError as e:
        return f"Speech recognition service error: {e}. Check your internet connection."
    except Exception as e:
        return f"An unexpected error occurred: {e}"