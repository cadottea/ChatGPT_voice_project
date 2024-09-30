import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300  # Adjust microphone sensitivity

# Test the microphone
with sr.Microphone() as source:
    print("Testing microphone... Speak now!")
    # audio = recognizer.listen(source)
    audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")