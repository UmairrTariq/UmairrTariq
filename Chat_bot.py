# --- Simple Python Chatbot Code ---

# Customize your chatbot's responses here!
# The key is what the user might say (or a keyword), and the value is the chatbot's reply.
responses = {
    "hello": "Hello there! How can I help you today?",
    "hi": "Hey! Nice to see you.",
    "how are you": "I'm a simple program, but I'm doing great! Thanks for asking.",
    "what is your name": "My name is Echo, a simple chatbot here to chat with you!",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "weather": "I can't check the weather, but I can tell you it's a great day for coding!",
    "thanks": "You're welcome!",
    "default": "I'm not sure I understand that. Try asking me something else!"
}

def get_response(user_input):
    """
    Checks the user's input for a keyword and returns the corresponding response.
    """
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return responses["default"]

def run_chatbot():
    """
    Main function to run the chatbot loop.
    """
    print("Echo: Hello! I'm a simple chatbot. Type 'exit' to end the chat.")
    while True:
        user_message = input("You: ")
        
        # Check for the exit command
        if user_message.lower() == "exit":
            print("Echo: Goodbye! Have a great day!")
            break
        
        # Get the bot's response
        bot_response = get_response(user_message)
        
        # Print the response
        print(f"Echo: {bot_response}")

# Run the chatbot!
if __name__ == "__main__":
    run_chatbot()