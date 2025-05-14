import os

from dotenv import load_dotenv 
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

# Check if the API key is set
if not api_key:
    print(
        "Please set your OPENAI_API_KEY environment variable to your hosted LLM's API key."
    )
else:

    def chat_with_llm(messages):
        try:
            client = OpenAI(
                base_url="https://llm.dev.aicore.team/api",  
                api_key=api_key,  
            )
            response = client.chat.completions.create(
                model="llama3-8b", 
                messages=messages,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    conversation_history = []

    print("Welcome to the chat! Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break

        conversation_history.append({"role": "user", "content": user_input})
        ai_response = chat_with_llm(conversation_history)

        if ai_response:
            print(f"AI: {ai_response}")
            conversation_history.append({"role": "assistant", "content": ai_response})
