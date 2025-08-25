from datetime import datetime
import random
def lads():
    print("Hey!!I'm LADS.\nYou can ask me things related to Kaushal.\nEnter 'info' to view all the commands")
    user_input = '' # Important Aspect for future
    exitCommands = ['exit','quit','end']
    commands = [
        "info      -   List of all commands",
        "about     -   To know about me",
        "contact   -   To know about how to connect",
        "skills    -   To know about the skills",
        "project   -   To know about projects",
        "time      -   Current date and time",
        "date      -   Current date and time",
        "exit      -   To terminate the code",
        "quit      -   To terminate the code",
        "end       -   To terminate the code"
    ]
    while user_input not in exitCommands:          #This logic will atleast run a loop once which will consume resources
        user_input = input("> ").lower().strip()

    # while(True):                                  #This logic is the solution for the above issue
    #     user_input = input("> ").lower()
    #     if(user_input != not in exitCommands):
    #         print("EXIT COMMAND ENTERED!!")
    #         break
        if user_input == 'info':
            # with open('chatbot.txt', 'r') as cmd:
            #     commands = cmd.readlines()
            #     for i,cmds in enumerate(commands, 1):
            #         print(f"{i}. {cmds.strip()}")
            
            for i in commands:
                print(f"{i}")
        elif (word in user_input for word in ["hello", "hii", "hey", "greet"]):
            response = [
                "Hello! How can I assist you today?",
                "Hi there! What can I help you with?",
                "Hey! How can I be of service?",
                "Greetings! How may I help you today?"
            ]
            print(f"{random.choice(response)}")
        elif user_input == 'about':
            print("""
Hii! Kaushal this side. I'm a 3rd year B.tech(CSE) student who is keen to learn new stuffs related to tech. This is my small part of the major project which I hope I will complete in near future.
                """)
        elif user_input == 'contact':
            print("""
GitHub - https://github.com/Nikk-Hub-Code/
E-Mail - jhakaushal.1809@gmail.com
LinkedIn - https://linkedin.com/in/nikk18/
                """)
        elif user_input == 'skills':
            print("""
1. Python
2. Front-End (HTML, CSS, JS)
3. WordPress
                """)
        elif user_input == 'project':
            print("""
1. To-Do list CLI
2. Lads (Learning & Working)
                """)
        elif user_input == 'date' or user_input == 'time':
            dateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"""
{dateTime}
                """)


if __name__ == "__main__":
    lads()
