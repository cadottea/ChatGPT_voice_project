# Initialize the recognizer
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

def chat():
    conversation_history = []
    print("ChatGPT: Hello! How can I assist you today?")

    while True:
        user_input = input("You: ")
        conversation_history.append({"role": "user", "content": user_input})

        try:
            # Create a chat completion request
            response = client.chat.completions.create(model="gpt-3.5-turbo", messages=conversation_history)

            assistant_message = response.choices[0].message.content
            print(f"ChatGPT: {assistant_message}")
            conversation_history.append({"role": "assistant", "content": assistant_message})

            # Simulate typing delay with randomness
            time.sleep(random.uniform(1, 3))

        except openai.RateLimitError:
            print("Rate limit exceeded. Please wait...")
            time.sleep(10)
        except Exception as e:
            print(f"An error occurred in Selenium voice function: {e}")
            print(f"An unexpected error occurred in chat function: {e}")
            print(traceback.format_exc())  # Print the full traceback
