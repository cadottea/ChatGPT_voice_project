# ChatGPT Voice Project

## Overview
The ChatGPT Voice Project allows users to interact with ChatGPT using voice input. It transcribes speech to text, processes the input through ChatGPT via a Selenium-powered browser automation, and provides responses. This project enhances accessibility and user convenience by integrating transcription and automated web interactions.

## Features
- Voice-to-Text Transcription: Uses SpeechRecognition and a microphone to transcribe speech into text.
- ChatGPT Integration: Sends transcribed text to ChatGPT through Selenium automation.
- Automated Workflow: Simulates typing the transcribed text into the ChatGPT input box and submits it via a browser session.

## Requirements
- Python 3.7 or higher
- Required Python packages: `selenium`, `webdriver-manager`, `SpeechRecognition`, `pyautogui`

## Installation
1. Clone the repository: `git clone https://github.com/cadottea/ChatGPT_voice_project.git` and `cd ChatGPT_voice_project`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Ensure you have **Google Chrome** installed on your system.

## Usage
1. Place the transcribed text file in the `transcriptions` folder: File name should be `transcription.txt`.
2. Run the script: `python main.py`
3. The script will: 
   - Read the text from `transcriptions/transcription.txt`.
   - Open ChatGPT in a browser using Selenium.
   - Simulate entering the text and submitting it to ChatGPT.
4. Observe the browser for the response. The browser will close automatically after the session.

## Known Issues
- Ensure the **ChatGPT login session** is active. The script does not handle the login process.
- The `transcriptions/transcription.txt` file must exist and contain the text to be sent.
- Browser automation may fail if **OpenAI’s website layout** changes.

## Customization
- Update the `file_path` variable in `main()` to specify a different location for the transcription file.
- Adjust the delay times in the `send_to_chatgpt()` function to match your system’s performance.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

## License
This project is licensed under the MIT License.