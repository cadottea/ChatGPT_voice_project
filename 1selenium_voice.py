import time
import speech_recognition as sr
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Selenium driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Navigate to the ChatGPT website
driver.get("https://chat.openai.com")

# Wait for the page to load
time.sleep(10)  # Adjust time based on your internet speed

# Set up the Speech Recognizer
recognizer = sr.Recognizer()

def listen_and_send():
    with sr.Microphone() as source:
        print("Please speak something...")
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            user_input = recognizer.recognize_google(audio)
            print(f"You said: {user_input}")

            # Find the text box and enter the recognized text
            input_box = driver.find_element("xpath", "//textarea")  # Adjust the xpath if needed
            input_box.send_keys(user_input)
            input_box.send_keys("\n")  # Press enter to send

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    while True:
        listen_and_send()
