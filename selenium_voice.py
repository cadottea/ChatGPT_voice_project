

import openai
import speech_recognition as sr

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
  # Uncomment this if you want to run it in headless mode
#chrome_options.add_argument("--headless")

# Set up the Chrome driver
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://chat.openai.com/")  # Open ChatGPT


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
    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print("You said: " + text)

        # Find the input box in ChatGPT and enter the text
        input_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea"))
        )
        input_box.send_keys(text)
        input_box.send_keys('\n')  # Press Enter to send the message
        print("Message sent to ChatGPT.")

        # Allow time for ChatGPT to respond
        time.sleep(5)  # Wait for the response to load (adjust as necessary)

        # Optionally, retrieve the response (this might require adjustments 
        # based on ChatGPT's structure)
        response_box = driver.find_element(By.CSS_SELECTOR, ".overflow-hidden")  # Adjust selector as needed
        response = response_box.text
        print("ChatGPT says: " + response)


    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        # Adding the current page source can help identify issues
        print(driver.page_source)  # Print the HTML of the page to see what's going on
    finally:
        driver.quit()  # Ensure the browser is closed after execution
