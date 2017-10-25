<<<<<<< HEAD
#!/usr/bin/python
import mysql.connector
=======
from collections import Counter
>>>>>>> 7c8de4a922e05c2726013ebf6c7d6dafb272ae7c

# User Codes
NOT_LOGGED_IN = 0
EDITOR = 1
AUTHOR = 2
REVIEWER = 3

USER_CODE = NOT_LOGGED_IN;
<<<<<<< HEAD
id = 1;
username = 'root'
password = 'password'
host = '127.0.0.1'
database = 'mydb'

command = raw_input("ManuscriptManager> ")

if USER_CODE == NOT_LOGGED_IN and command[0:15] == "register editor":
=======
id = 1; # TODO: get rid of this when db is providing pk's


while True:

    command = raw_input("ManuscriptManager> ")

    if USER_CODE == NOT_LOGGED_IN and command[0:15] == "register editor":
>>>>>>> 7c8de4a922e05c2726013ebf6c7d6dafb272ae7c
        first_name = raw_input("ManuscriptManager> Enter your first name: ")
        last_name = raw_input("ManuscriptManager> Enter your last name: ")
        if first_name == "" or last_name == "":
            print("Registration failed. Make sure you enter a value for each field.")
        else:
<<<<<<< HEAD
            connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
            cursor = connection.cursor()
            query = "INSERT INTO editor (firstName, middleInitial, lastName) VALUES (\"" + first_name + "\",\"\",\" " + last_name + "\")"
            cursor.execute(query)

            id = cursor.lastrowid # id of last added row
            connection.commit()
            cursor.close()
            connection.close()

            print("Welcome " + first_name + "! Your id for login is " + str(id) + ".")

elif USER_CODE == NOT_LOGGED_IN and command[0:15] == "register author":
=======
            # add to database editor: first name, last name, id (which is a global)
            # set the variable id = whatever id the DB generated
            print("Welcome! Your id for login is " + str(id) + ".")
            id = id + 1 # TODO: get rid of this when we have the db pk's working


    elif USER_CODE == NOT_LOGGED_IN and command[0:15] == "register author":
>>>>>>> 7c8de4a922e05c2726013ebf6c7d6dafb272ae7c
        first_name = raw_input("ManuscriptManager> Enter your first name: ")
        last_name = raw_input("ManuscriptManager> Enter your last name: ")
        email = raw_input("ManuscriptManager> Enter your email: ")
        address = raw_input("ManuscriptManager> Enter your address: ")
        affiliation = raw_input("ManuscriptManager> Enter your affiliation: ")
        if first_name == "" or last_name == "" or email == "" or address == "" or affiliation == "":
            print("Registration failed. Make sure you enter a value for each field.")
        else:
            # add to author table
            # set the variable id = whatever id the DB generated
            print("Welcome! Your id for login is " + str(id) + ".")
            id = id + 1  # TODO: get rid of this when we have the db pk's working

<<<<<<< HEAD
elif USER_CODE == NOT_LOGGED_IN and command[0:17] == "register reviewer":
=======
    elif USER_CODE == NOT_LOGGED_IN and command[0:17] == "register reviewer":
>>>>>>> 7c8de4a922e05c2726013ebf6c7d6dafb272ae7c
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

    # and so on and so forth

<<<<<<< HEAD
else:
     print("Invalid command.")
=======
    else:
        print("Invalid command.")








>>>>>>> 7c8de4a922e05c2726013ebf6c7d6dafb272ae7c

