import speech_recognition as sr
import pyautogui
import time

# Initialize the recognizer
recognizer = sr.Recognizer()

# Adjust recognizer sensitivity to ambient noise
recognizer.energy_threshold = 300

# Give you a little time to switch to the ChatGPT window
print("Switch to the ChatGPT window within 5 seconds...")
time.sleep(5)

with sr.Microphone() as source:
    print("Listening...")
    # audio = recognizer.listen(source)
    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print("You said: " + text)

        # Simulate typing the recognized text into the active window
        pyautogui.typewrite(text)
        pyautogui.press('enter')  # To send the message
        
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")