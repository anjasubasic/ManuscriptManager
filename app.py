#!/usr/bin/python
import mysql.connector

# User Codes
NOT_LOGGED_IN = 0
EDITOR = 1
AUTHOR = 2
REVIEWER = 3

user_code = NOT_LOGGED_IN;
id_of_logged_in_user = -1

username = 'root'
password = 'password'
host = '127.0.0.1'
database = 'mydb'

# # # STATUS COMMAND # # #
def status_print(user_type, id):
    connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
    cursor = connection.cursor()

    if user_type == AUTHOR:
        query = "SELECT A.status, M.title " \
                "FROM anyauthormanuscripts A " \
                "INNER JOIN manuscript M on M.idManuscript = A.idManuscript " \
                "WHERE idAuthor = " + str(id)
        cursor.execute(query)

        for (status, title) in cursor:
            print("# {}, {}".format(title, status))

    elif user_type == EDITOR:
        query = "SELECT * " \
                "FROM whatsleft " \
                "ORDER BY status, idManuscript"
        cursor.execute(query)

        for (manuscript, status, timestamp) in cursor:
            print("# {}, {}, {}".format(status, manuscript, timestamp))

    elif user_type == REVIEWER:
        query = "SELECT M.status, M.title " \
                "FROM manuscript M " \
                "INNER JOIN feedback F ON F.Manuscript_idManuscript = M.idManuscript " \
                "WHERE F.Reviewer_idReviewer =" + str(id)
        cursor.execute(query)

        for (status, title) in cursor:
            print("# {}, {}".format(status, title))

    connection.close()

while True:

    command = raw_input("ManuscriptManager> ")

    # # # REGISTER # # #
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
            id_of_logged_in_user = id

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
            id_of_logged_in_user = id

    elif user_code == NOT_LOGGED_IN and command[0:17] == "register reviewer":

        first_name = raw_input("ManuscriptManager> Enter your first name: ")
        last_name = raw_input("ManuscriptManager> Enter your last name: ")
        middle_initial = raw_input("ManuscriptManager> Enter your middle initial: ")
        affiliation = raw_input("ManuscriptManager> Enter your affiliation: ")
        email = raw_input("ManuscriptManager> Enter your email address: ")
        ri_codes = raw_input("ManuscriptManager> Enter 1 to 3 RICodes separated by the '/' character: ")
        ri_codes_list = ri_codes.split('/')
        num_of_entered_ri_codes = len(ri_codes_list)

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

                formattedRICodeList = ""

                for idx, code in enumerate(ri_codes_list):
                    formattedRICodeList = formattedRICodeList + "\"" + code + "\""
                    if idx < len(ri_codes_list) - 1:
                        formattedRICodeList = formattedRICodeList + ","


                # Get RICode ids for selected interests
                get_ricode_ids_query = "SELECT idRICode FROM ricode WHERE RIValue IN (" + formattedRICodeList + ")"
                cursor.execute(get_ricode_ids_query)

                ri_codes = [item[0] for item in cursor.fetchall()] # Gets all three RI Codes. cursor.fetchall() returns tuples, this only gets the value of each item

                # Format input for interest table
                formatted_input_list = ""

                for idx, code in enumerate(ri_codes):
                    formatted_input_list = formatted_input_list + "(" + str(idReviewer) + "," + str(code) + ")"
                    if idx < len(ri_codes) - 1:
                        formatted_input_list = formatted_input_list + ","

                # Add to interest table
                add_interest_query = "INSERT INTO interest VALUES " + formatted_input_list
                cursor.execute(add_interest_query)

                connection.commit()
                print("Welcome! Your id for login is " + str(idReviewer) + ".")
                id_of_logged_in_user = id

    # # # LOGIN # # #
    elif user_code == NOT_LOGGED_IN and command[0:5] == "login":
        role = raw_input("ManuscriptManager> Enter your role (editor/reviewer/author): ")
        id = raw_input("ManuscriptManager> Enter your id for log-in: ")

        # If role is valid, check if id is in the table for that role
        if role == "editor" or role == "reviewer" or role == "author":
            connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
            cursor = connection.cursor(buffered=True)
            find_id_query = "SELECT * FROM " + role + " WHERE id" + role + " = " + id
            cursor.execute(find_id_query)

            # If id exists in the table, proceed
            if cursor.rowcount == 1:
                if role == "editor":
                    editor_data = cursor.fetchone()
                    editor_id = editor_data[0]
                    editor_name = editor_data[1] + " " + editor_data[3]

                    print("Hi, " + editor_name + ".")
                    user_code = EDITOR
                    id_of_logged_in_user = editor_id
                    status_print(EDITOR, editor_id)

                elif role == "reviewer":
                    reviewer_data = cursor.fetchone()
                    reviewer_id = reviewer_data[0]
                    reviewer_name = reviewer_data[1] + " " + reviewer_data[5]

                    print("Hi, " + reviewer_name + ".")
                    user_code = REVIEWER
                    id_of_logged_in_user = reviewer_id
                    status_print(REVIEWER, reviewer_id)

                elif role == "author":
                    author_data = cursor.fetchone()

                    author_name = author_data[1] + " " + author_data[6]
                    author_address = author_data[3]
                    author_id = author_data[0]
                    print("Hi, " + author_name + ". Your address is: " + author_address + ".")
                    user_code = AUTHOR
                    id_of_logged_in_user = author_id
                    status_print(AUTHOR, author_id)
            else:
                print("That id does not exist.")
        else:
            print("That is not a valid role.")

    # # # Author-specific commands # # #
    elif user_code == AUTHOR and command[0:6] == "submit":
        title = raw_input("ManuscriptManager> Enter title of paper: ")
        affiliation = raw_input("ManuscriptManager> Enter your affiliation for this paper: ")
        ri_code = raw_input("ManuscriptManager> Enter the RICode for this paper: ")
        author2 = raw_input("ManuscriptManager> Enter the second author for this paper (leave blank if no second author): ")
        author3 = raw_input("ManuscriptManager> Enter the third author for this paper (leave blank if no third author): ")
        author4 = raw_input("ManuscriptManager> Enter the fourth author for this paper (leave blank if no fourth author): ")
        filename = raw_input("ManuscriptManager> Enter your paper's filename: ")
        if title == "" or affiliation == "" or ri_code == "" or filename == "":
            print("Submission failed. One or more required fields were left blank.")
        elif os.path.isFile(filename) == 0:  # invalid file
            print("Submission failed. The specified file does not exist in your current directory.")
        else: # invalid ri code
            connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
            cursor = connection.cursor(buffered=True)
            validate_interests_query = "SELECT COUNT(idRICode) FROM ricode WHERE RIValue IN (\"" + ri_code + "\")"
            cursor.execute(validate_interests_query)
            if cursor.fetchone()[0] == 0:
                print("Submission failed. Invalid RICode.")
            else: # ri code was valid
                # add submission to db (see details on assignment page)
                manuscript_id = -1 # this is just a placeholder. to be changed based on what the db comes up with
                print("Submission successful. Your manuscript's id is: " + manuscript_id)
            connection.close()

    elif user_code == AUTHOR and command[0:6] == "status":
        status_print(AUTHOR, id_of_logged_in_user)

    elif user_code == AUTHOR and command[0:7] == "retract":
        manuscript_id = raw_input("ManuscriptManager> Enter manuscript ID: ")
        are_you_sure = raw_input("ManuscriptManager> Are you sure you want to delete this manuscript? (y/n): ")
        if are_you_sure == "n":
            print("Canceled retraction")
        elif are_you_sure == "y":
            


    else:
        print("Invalid command.")

