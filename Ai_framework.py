import random

def greet_user():
    greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!", "Welcome!"]
    return random.choice(greetings)

def farewell_user():
    farewells = ["Goodbye!", "See you later!", "Bye!", "Take care!", "Have a great day!"]
    return random.choice(farewells)

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    responses = {
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I'm a chatbot created to assist you!",
        "what can you do": "I can chat with you, answer simple questions, and keep you entertained!",
        "tell me a joke": "Why don’t skeletons fight each other? Because they don’t have the guts!",
        "bye": farewell_user()
    }
    
    for key in responses:
        if key in user_input:
            return responses[key]
    
    return "I'm not sure how to respond to that."

def main():
    print(greet_user())
    print("I'm your friendly chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "bye":
            print(farewell_user())
            break
        
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        
if __name__ == "__main__":
    main()
