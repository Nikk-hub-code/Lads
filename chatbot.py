from datetime import datetime
import random

class LADS:
    def __init__(self):
        self.exit_commands = ['exit', 'quit', 'end', 'bye']
        self.positive_words = ['good', 'happy', 'great', 'awesome', 'fantastic', 'wonderful']
        self.negative_words = ['bad', 'sad', 'terrible', 'awful', 'horrible', 'unhappy']
        self.greeting_words = ["hello", "hi", "hey", "greetings", "howdy", "hola"]
        
        self.commands = {
            "info": "List of all commands",
            "about": "To know about me",
            "contact": "To know about how to connect",
            "skills": "To know about the skills",
            "project": "To know about projects",
            "time": "Current date and time",
            "date": "Current date and time",
            "exit": "To terminate the code",
            "quit": "To terminate the code",
            "end": "To terminate the code"
        }
        
        self.greeting_responses = [
            "Hello! How can I assist you today?",
            "Hi there! What can I help you with?",
            "Hey! How can I be of service?",
            "Greetings! How may I help you today?"
        ]
        
        self.unknown_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "I don't recognize that command. Type 'info' to see what I can do.",
            "Sorry, I didn't get that. Try asking me something else.",
            "I'm still learning. Could you try a different question?"
        ]

    def display_welcome(self):
        print("=" * 50)
        print("Hey!! I'm LADS.")
        print("You can ask me things related to Kaushal.")
        print("Enter 'info' to view all the commands")
        print("=" * 50)

    def display_info(self):
        print("\nAvailable commands:")
        print("-" * 30)
        for cmd, desc in self.commands.items():
            print(f"{cmd.ljust(10)} - {desc}")
        print()

    def display_about(self):
        print("""
Hii! Kaushal this side. I'm a 3rd year B.tech(CSE) student who is keen to learn 
new stuff related to tech. This is my small part of the major project which 
I hope I will complete in the near future.
        """)

    def display_contact(self):
        print("""
GitHub - https://github.com/Nikk-Hub-Code/
E-Mail - jhakaushal.1809@gmail.com
LinkedIn - https://linkedin.com/in/nikk18/
        """)

    def display_skills(self):
        print("""
1. Python
2. Front-End (HTML, CSS, JS)
3. WordPress
4. Problem Solving
        """)

    def display_projects(self):
        print("""
1. To-Do list CLI
2. Lads (Learning & Working)
3. Several web development projects(Portfolio, Counter, etc.)
        """)

    def display_time(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\nCurrent date and time: {current_time}\n")

    def analyze_sentiment(self, text):
        positive_count = sum(1 for word in self.positive_words if word in text)
        negative_count = sum(1 for word in self.negative_words if word in text)
        
        if positive_count > negative_count:
            return "positive"
        elif negative_count > positive_count:
            return "negative"
        else:
            return "neutral"

    def process_input(self, user_input):
        # Clean and normalize input
        cleaned_input = user_input.lower().strip()
        
        # Check for exit commands
        if cleaned_input in self.exit_commands:
            return "exit"
            
        # Check for greetings
        if any(word in cleaned_input for word in self.greeting_words):
            return print(random.choice(self.greeting_responses))
            
        # Check for specific commands
        if cleaned_input == "info":
            self.display_info()
            return "command_executed"
        elif cleaned_input == "about":
            self.display_about()
            return "command_executed"
        elif cleaned_input == "contact":
            self.display_contact()
            return "command_executed"
        elif cleaned_input == "skills":
            self.display_skills()
            return "command_executed"
        elif cleaned_input == "project":
            self.display_projects()
            return "command_executed"
        elif cleaned_input in ["time", "date"]:
            self.display_time()
            return "command_executed"
            
        # If no specific command matched
        return "unknown"

    def run(self):
        self.display_welcome()
        
        while True:
            try:
                user_input = input("> ").strip()
                
                if not user_input:
                    continue
                    
                result = self.process_input(user_input)
                
                if result == "exit":
                    print("Goodbye! Have a great day!")
                    break
                elif result == "unknown":
                    print(random.choice(self.unknown_responses))
                    
                # Analyze sentiment for any input
                sentiment = self.analyze_sentiment(user_input)
                if sentiment == "positive":
                    print("That sounds positive! 😊")
                elif sentiment == "negative":
                    print("I'm sorry to hear that. 😔")
                    
            except KeyboardInterrupt:
                print("\n\nInterrupted by user. Goodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")

def main():
    chatbot = LADS()
    chatbot.run()

if __name__ == "__main__":
    main()
