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
        middle_initial = raw_input("ManuscriptManager> Enter your middle initial: ")
        affiliation = raw_input("ManuscriptManager> Enter your affiliation: ")
        email = raw_input("ManuscriptManager> Enter your email address: ")
        ri_codes = raw_input("ManuscriptManager> Enter 1 to 3 RICodes separated by the '/' character: ")
        ri_codes_list = ri_codes.split('/')
        num_of_entered_ri_codes = len(ri_codes_list)
        print(num_of_entered_ri_codes)

        if first_name == "" or last_name == "" or ri_codes == "":
            print("Registration failed. Make sure you enter a value for each field.")

        # Number of valid codes must be 3 for reviewer to register
        elif num_of_entered_ri_codes > 3:
            print("Registration failed. Make sure you enter valid RI codes.")

        else:

            connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
            cursor = connection.cursor(buffered=True)
            # Gets number of valid interests:
            num_of_valid_codes = 0
            for code in ri_codes_list:
                validate_interests_query = "SELECT COUNT(idRICode) FROM ricode WHERE RIValue IN (\"" + code + "\")"
                cursor.execute(validate_interests_query)
                if cursor.fetchone()[0] == 1:
                    num_of_valid_codes = num_of_valid_codes + 1
                connection.close()

            if num_of_valid_codes != num_of_entered_ri_codes:
                print("Registration failed. You have entered one or more invalid RICodes.")

            else:

                connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
                cursor = connection.cursor(buffered=True)
                # Add reviewer
                add_reviewer_query = "INSERT INTO reviewer (firstName, emailAddress, currentAffiliation, middleInitial, lastName) " \
                    " VALUES (\"" + first_name + "\", \"" + email + "\", \"" + affiliation + "\", \"" + middle_initial + "\", \"" + last_name + "\") "
                cursor.execute(add_reviewer_query)
                connection.commit()

                idReviewer = cursor.lastrowid

                # Get RICode ids for selected interests
                get_ricode_ids_query = "SELECT idRICode FROM ricode WHERE RIValue IN (\"" + ri_code1 + "\", \"" + ri_code2 + "\", \"" + ri_code3 + "\")"
                cursor.execute(get_ricode_ids_query)

                ri_codes = [item[0] for item in cursor.fetchall()] # Gets all three RI Codes. cursor.fetchall() returns tuples, this only gets the value of each item

                # Add to interest table
                add_interest_query = "INSERT INTO interest VALUES (\"" + str(idReviewer) + "\", \"" + str(ri_codes[0]) + "\"), " \
                                                            " (\"" + str(idReviewer) + "\", \"" + str(ri_codes[1]) + "\"), " \
                                                            " (\"" + str(idReviewer) + "\", \"" + str(ri_codes[2]) + "\") "
                cursor.execute(add_interest_query)

                connection.commit()
                print("Welcome! Your id for login is " + str(idReviewer) + ".")

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

