def lads():
    print("Hey!!I'm LADS.\nYou can ask me things related to Kaushal.\nEnter 'info' to view all the commands")
    user_input = '' # Important Aspect for future
    exitCommands = ['exit','quit','end']
    commands = [
        "info",
        "about",
        "contact",
        "skills",
        "projects",
        "exit",
        "quit",
        "end"
    ]
    while user_input not in exitCommands:          #This logic will atleast run a loop once which will consume resources
        user_input = input("> ").lower()
        
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
        elif user_input == 'about':
            print("About")
        elif user_input == 'contact':
            print("contact")
        elif user_input == 'skills':
            print("skills")
        elif user_input == 'projects':
            print("projects")


if __name__ == "__main__":
    lads()
