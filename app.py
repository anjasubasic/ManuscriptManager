# User Codes
NOT_LOGGED_IN = 0
EDITOR = 1
AUTHOR = 2
REVIEWER = 3

USER_CODE = NOT_LOGGED_IN;
id = 1;


while True:

    command = raw_input("ManuscriptManager> ")

    if USER_CODE == NOT_LOGGED_IN and command[0:15] == "register editor": # this is sort of hacky, but..
        print("hi")

    elif USER_CODE == NOT_LOGGED_IN and command[0:15] == "register author":
        print("hi")

    elif USER_CODE == NOT_LOGGED_IN and command[0:17] == "register reviewer":
        print("hi")

    # and so on and so forth

    else:
        print("Invalid command.")







