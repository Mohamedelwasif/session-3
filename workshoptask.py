import random

class Chatbot:
    def __init__(self, name="Machine Learning Bot"):
        # Predefined responses
        self.name = name
        self.responses = {
            "hello": ["Hello!", "Hi there!", "Greetings!"],
            "how are you": ["I'm doing well, thank you!", "I'm fine, how about you?"],
            "goodbye": ["Goodbye!", "See you later!", "Farewell!"],
            "default": ["I'm sorry, I didn't understand.", "Could you please rephrase that?"]
        }

    def get_response(self, user_input):
        # Method to get a response based on user input
        for key in self.responses:
            if key in user_input.lower():
                return random.choice(self.responses[key])
        return random.choice(self.responses["default"])

    def start_chat(self):
        # Method to start the chatbot interaction
        print(f"{self.name}: Hi! How can I assist you today?")
        
        predefined_inputs = [
            "Hello chatbot",
            "How are you doing?",
            "Goodbye"
        ]
        
        for user_input in predefined_inputs:
            print(f"User: {user_input}")
            response = self.get_response(user_input)
            print(f"{self.name}: {response}")
            
            if user_input.lower() == "goodbye":
                break

# Create an instance of the Chatbot class and run it
chatbot_instance = Chatbot()
chatbot_instance.start_chat()
