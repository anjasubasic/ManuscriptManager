#!/usr/bin/python
import mysql.connector

# User Codes
NOT_LOGGED_IN = 0
EDITOR = 1
AUTHOR = 2
REVIEWER = 3

user_code = NOT_LOGGED_IN;
id = 1; # TODO: get rid of this when db is providing pk's
id_of_logged_in_user = -1

username = 'root'
password = 'password'
host = '127.0.0.1'
database = 'mydb'

def status_print(user_type):
    if user_type == AUTHOR:
        print("hi")
    elif user_type == EDITOR:
        print("hi")
    elif user_type == REVIEWER:
        print("hi")

while True:

    command = raw_input("ManuscriptManager> ")

    if user_code == NOT_LOGGED_IN and command[0:15] == "register editor":

        first_name = raw_input("ManuscriptManager> Enter your first name: ")
        last_name = raw_input("ManuscriptManager> Enter your last name: ")
        if first_name == "" or last_name == "":
            print("Registration failed. Make sure you enter a value for each field.")
        else:
            connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
            cursor = connection.cursor()
            query = "INSERT INTO editor (firstName, middleInitial, lastName) VALUES (\"" + first_name + "\",\"\",\" " + last_name + "\")"
            cursor.execute(query)

            id = cursor.lastrowid # id of last added row
            connection.commit()
            cursor.close()
            connection.close()

            print("Welcome " + first_name + "! Your id for login is " + str(id) + ".")

    elif user_code == NOT_LOGGED_IN and command[0:15] == "register author":

        first_name = raw_input("ManuscriptManager> Enter your first name: ")
        middle_initial = raw_input("ManuscriptManager> Enter your middle initial: ")
        last_name = raw_input("ManuscriptManager> Enter your last name: ")
        email = raw_input("ManuscriptManager> Enter your email: ")
        address = raw_input("ManuscriptManager> Enter your address: ")
        affiliation = raw_input("ManuscriptManager> Enter your affiliation: ")
        if first_name == "" or last_name == "" or email == "" or address == "" or affiliation == "":
            print("Registration failed. Make sure you enter a value for each field.")
        else:
            connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
            cursor = connection.cursor()

            query = "INSERT INTO author (firstName, emailAddress, mailingAddress, currentAffiliation, middleInitial, lastName) " \
                    " VALUES (\"" + first_name + "\", \"" + email + "\", \"" + address+ "\", \"" + affiliation + "\", \"" + middle_initial+ "\", \"" + last_name + "\")"

            cursor.execute(query)

            id = cursor.lastrowid  # id of last added row
            connection.commit()
            cursor.close()
            connection.close()
            print("Welcome " + first_name + "! Your id for login is " + str(id) + ".")

    elif user_code == NOT_LOGGED_IN and command[0:17] == "register reviewer":

        first_name = raw_input("ManuscriptManager> Enter your first name: ")
        last_name = raw_input("ManuscriptManager> Enter your last name: ")
        ri_codes = raw_input("ManuscriptManager> Enter 1 to 3 RICodes separated by spaces: ")
        ri_codes_list = ri_codes.split()
        if first_name == "" or last_name == "" or ri_codes == "":
            print("Registration failed. Make sure you enter a value for each field.")
        elif len(ri_codes_list) > 3:
            print("Registration failed. You can't enter more than 3 RICodes.")
        # verify that RICodes are "valid" print failure message if not valid
        else:
            # add to reviewer table, index into ri_codes_list to get each ri code
            # set the variable id = whatever id the DB generated
            print("Welcome! Your id for login is " + str(id) + ".")
            id = id + 1  # TODO: get rid of this when we have the db pk's working

    elif user_code == NOT_LOGGED_IN and command[0:5] == "login":
        id = raw_input("ManuscriptManager> Enter your id for log-in: ")
        #if id is in author table
            # author_name = <get full author name from db>
            # author_address = <get author address from db>
            # print("Thanks for logging in!")
            # print("Your name is " + author_name + ".")
            # print("Your address is " + author_address + ".")
            # status_print(AUTHOR)
            # user_code = AUTHOR
            # id_of_logged_in_user = id
        #elif id is in editor table
            # editor_name = <get full editor name>
            # print("Thanks for logging in!")
            # print("Your name is " + editor_name + ".")
            # status_print(EDITOR)
            # user_code = EDITOR
            # id_of_logged_in_user = id
        #elif id is in reviewer table
            # reviewer_name = <get full reviewer name>
            # print("Thanks for logging in!")
            # print("Your name is " + reviewer_name + ".")
            # status_print(REVIEWER)
            # user_code = REVIEWER
            # id_of_logged_in_user = id
        #else:
        print("That id does not exist.")


    # and so on and so forth

    else:
        print("Invalid command.")

