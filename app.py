import google.generativeai as genai
import os

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

def main():
    print("Chat with Gemini! Type 'Exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting chat.")
            break
        response = chat.send_message(user_input)
        print("Gemini:", response.text)

if __name__ == "__main__":
    main()
