from collections import Counter

# User Codes
NOT_LOGGED_IN = 0
EDITOR = 1
AUTHOR = 2
REVIEWER = 3

USER_CODE = NOT_LOGGED_IN;
id = 1;


while True:

    command = raw_input("ManuscriptManager> ")

    if USER_CODE == NOT_LOGGED_IN and command[0:15] == "register editor":
        word_list = command.split() # word list can be indexed into to get each word in the command
        word_count = len(word_list)
        if word_count != 4:
            print("Please use the format 'register editor <first name> <last name>")
        else:
            # add to database editor: first name, last name, id (which is a global)
            print("Welcome! Your id for login is " + str(id) + ".")
            id = id + 1 # increment the global id variable so that we always have unique id's

    elif USER_CODE == NOT_LOGGED_IN and command[0:15] == "register author":
        print("hi")

    elif USER_CODE == NOT_LOGGED_IN and command[0:17] == "register reviewer":
        print("hi")

    # and so on and so forth

    else:
        print("Invalid command.")









