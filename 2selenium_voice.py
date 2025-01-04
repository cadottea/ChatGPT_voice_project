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
        EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea"))  # This checks if the element is clickable
        )

        #input_box = WebDriverWait(driver, 10).until(
        #EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))  # Adjust the selector as needed
        #)
        
        # Initialize speech recognition
        with sr.Microphone() as source:
            print("Listening...")
            r = sr.Recognizer()
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            #audio = r.listen(source)

            # Convert audio to text
            user_input = r.recognize_google(audio)
            print(f"You said: {user_input}")

            time.sleep(2)  # Adjust the delay as needed
            input_box.send_keys(user_input)
            input_box.send_keys(Keys.RETURN)  # Simulate pressing Enter

    except Exception as e:
        print(f"An error occurred in Selenium voice function: {e}")
        print(traceback.format_exc())  # Print the full traceback
        if driver:  # Only print the page source if the driver is initialized
            print(driver.page_source[:100])
            #print(driver.page_source)  # Print the current page source for debugging
    finally:
        if driver:  # Ensure the driver is closed if it was created
            driver.quit()  # Always close the driver at the end

if __name__ == "__main__":
    # You can uncomment either one of these based on your testing preference
    # chat()
    run_selenium_voice()
