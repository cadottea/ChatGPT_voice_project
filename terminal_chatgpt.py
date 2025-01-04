import os
from openai import OpenAI
#import openai
import time
import random

# Load the API key from the environment variable
#openai.api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def chat():
    conversation_history = []
    print("ChatGPT: Hello! How can I assist you today?")

    while True:
        user_input = input("You: ")
        conversation_history.append({"role": "user", "content": user_input})

        try:
            # Create a chat completion request
            #response = openai.ChatCompletion.create(
            chat_completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=conversation_history
            )

            assistant_message = response['choices'][0]['message']['content']
            print(f"ChatGPT: {assistant_message}")
            conversation_history.append({"role": "assistant", "content": assistant_message})

            # Simulate typing delay with randomness
            time.sleep(random.uniform(1, 3))  # Wait for 1 to 3 seconds

        except openai.RateLimitError:
            print("Rate limit exceeded. Please wait...")
            time.sleep(10)  # Wait longer if rate limit is hit
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    chat()
