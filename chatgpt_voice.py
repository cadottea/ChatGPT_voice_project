import openai
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import webbrowser
import time

# Set up the Chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://chat.openai.com/")  # Open ChatGPT

# Open the ChatGPT website
webbrowser.open('https://chat.openai.com')  # Replace with the ChatGPT URL if necessary

# Allow time for the browser to open
time.sleep(5)  # Adjust the sleep time as needed

# Set your OpenAI API key here

# Initialize the recognizer
recognizer = sr.Recognizer()

# Adjust recognizer sensitivity to ambient noise
# You can increase or decrease this value based on your environment
recognizer.energy_threshold = 300

with sr.Microphone() as source:
    print("Listening...")
    # audio = recognizer.listen(source)
    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        # Recognize speech using Google Web Speech API
        #text = recognizer.recognize_google(audio)
        #print("You said: " + text)

        # Adjust the selector if necessary
        input_box = driver.find_element(By.CSS_SELECTOR, "textarea")
        input_box.send_keys(text)

        # Send the text to OpenAI API

        # response = openai.ChatCompletion.create(
        # response = openai.completions.create(
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": text}
            ]
        )
        # print(response)
        print("Raw response:", response)  # To see the full response structure



        # Print the response from OpenAI
        print("ChatGPT says: " + response['choices'][0]['message']['content'])
    except openai.RateLimitError:
        print("You've reached your usage limit. Please check your OpenAI account for more details.")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
