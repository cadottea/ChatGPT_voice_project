import os
import openai
from openai import OpenAI
import time
import random
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import speech_recognition as sr
from selenium.webdriver.common.keys import Keys

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Initialize the recognizer
recognizer = sr.Recognizer()

def run_selenium_voice():
    driver = None
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://chat.openai.com")

        # Wait for the input box to be present
        input_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea"))
        )

        # Initialize speech recognition
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)  # Adjusted timeout and phrase_time_limit

            # Convert audio to text
            try:
                user_input = recognizer.recognize_google(audio)
                print(f"You said: {user_input}")

                # Send input to the chat
                time.sleep(2)  # Adjust the delay as needed
                input_box.send_keys(user_input)
                input_box.send_keys(Keys.RETURN)  # Simulate pressing Enter
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

    except Exception as e:
        print(f"An error occurred in Selenium voice function: {e}")
        print(traceback.format_exc())  # Print the full traceback
        if driver:  # Only print the page source if the driver is initialized
            print(driver.page_source[:100])  # Print part of the page source for debugging
    finally:
        if driver:  # Ensure the driver is closed if it was created
            driver.quit()  # Always close the driver at the end

if __name__ == "__main__":
    run_selenium_voice()
