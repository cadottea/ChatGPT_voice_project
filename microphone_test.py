import os
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300  # Adjust microphone sensitivity

# Define the directory to save the file
folder_path = "transcriptions"
os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exist


# Test the microphone
with sr.Microphone() as source:
    print("Testing microphone... Speak now!")
    # audio = recognizer.listen(source)
    audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)

    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print("You said: " + text)

        # Save transcription to a text file
        file_path = os.path.join(folder_path, "transcription.txt")
        with open(file_path, "w") as file:
            file.write(text)
        print(f"Transcription saved to {file_path}")

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")