import os
import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Function to send text to ChatGPT
def send_to_chatgpt(text):
    driver = None
    try:
        # Set up Chrome WebDriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://chat.openai.com")

        # Wait for the page to load
        time.sleep(1)  # Initial wait time

        # Wait for the input box to be present
        input_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[contenteditable='true']"))
        )
        print("Input box found.")

        # Focus on the input box
        driver.execute_script("arguments[0].focus();", input_box)
        time.sleep(0.5)  # Brief pause to ensure focus is registered

        # Simulate typing the transcription into the input box
        input_box.send_keys(text)

        # Wait briefly to ensure the text is entered
        time.sleep(0.5)

        # Use JavaScript to simulate Enter key press
        #driver.execute_script("var evt = new KeyboardEvent('keydown', { bubbles: true, cancelable: true, key: 'Enter', char: 'Enter', keyCode: 13 }); arguments[0].dispatchEvent(evt);", input_box)
        driver.execute_script("arguments[0].click();", enter_button)


        # Wait for a while to ensure the message is sent
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")
        print(traceback.format_exc())

    finally:
        # Close the browser after a delay for observation
        if driver:
            time.sleep(3)
            driver.quit()

# Test function to read from a text file and send the content to ChatGPT
def main():
    try:
        # Specify the file path for the transcribed text file
        file_path = "transcriptions/transcription.txt"

        # Read the text from the file
        with open(file_path, "r") as file:
            transcription_text = file.read()

        # Print the text to confirm it was read correctly
        print(f"Transcription text: {transcription_text}")

        # Send the text to ChatGPT
        send_to_chatgpt(transcription_text)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
        print(traceback.format_exc())

if __name__ == "__main__":
    main()
