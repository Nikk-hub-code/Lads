def lads():
    print("Hey!!I'm LADS.\nYou can ask me things related to Kaushal.\nEnter 'info' to view all the commands")
    user_input = '' # Important Aspect for future
    exitCommands = ['exit']
    while user_input not in exitCommands:          #This logic will atleast run a loop once which will consume resources
        user_input = input("> ").lower()
    # while(True):                                  #This logic is the solution for the above issue
    #     user_input = input("> ").lower()
    #     if(user_input != not in exitCommands):
    #         print("EXIT COMMAND ENTERED!!")
    #         break


if __name__ == "__main__":
    lads()
