# Define responses
responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! How can I assist you?",
    "how are you": "I'm a chatbot, so I don't have feelings, but I'm here to help you!",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I don't understand that."
}

# Function to get response
def get_response(user_input):
    user_input = user_input.lower()  # Convert the input to lowercase
    return responses.get(user_input, responses["default"])

# Chat loop
def chat():
    print("Chatbot: Hi! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chat()
