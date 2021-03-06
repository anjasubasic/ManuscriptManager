#!/usr/bin/python
import datetime
import mysql.connector

# User Codes / Table ids
import os

NOT_LOGGED_IN = 0
EDITOR = 1
AUTHOR = 2
REVIEWER = 3

# Other table ids
MANUSCRIPT = 4

# state variables
user_code = NOT_LOGGED_IN;
id_of_logged_in_user = -1

# constants
username = 'root'
password = 'password'
host = '127.0.0.1'
database = 'mydb'

############################
# # # HELPER FUNCTIONS # # #
############################

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
        query = "SELECT idManuscript, status, date(statusModifiedDateTime) " \
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

# should return true if the id is in the corresponding db, false else
def id_is_valid(table, id):

    table_name = ""
    if table == AUTHOR:
        table_name = "author"
    elif table == EDITOR:
        table_name = "editor"
    elif table == REVIEWER:
        table_name = "reviewer"
    elif table == MANUSCRIPT:
        table_name = "manuscript"

    if id.isdigit():
        connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
        cursor = connection.cursor(buffered=True)
        find_id_query = "SELECT * FROM " + table_name + " WHERE id" + table_name + " = " + id
        cursor.execute(find_id_query)

        # If id exists in the table, return true
        if cursor.rowcount == 1:
            return True

        return False

    else:
        "Entered value is not an integer."
        return False

# returns true if the given string can be cast to an int
def could_be_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

# returns true if manuscript has been typeset, false else
def manuscript_is_typeset(manuscript_id):
    connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
    cursor = connection.cursor(buffered=True)

    # returns a row if manuscript is scheduled for publication, published or in typesetting. Otherwise returns 0 rows
    find_id_query = "SELECT * " \
                    "FROM manuscript " \
                    "WHERE idManuscript = " + str(manuscript_id) + " AND status IN (\"scheduled for publication\", \"published\", \"in typesetting\")"
    cursor.execute(find_id_query)

    if cursor.rowcount == 1:
        cursor.close()
        connection.close()
        return True # manuscript is in typsetting/scheduled for publication/published

    cursor.close()
    connection.close()

    return False

# returns number of reviews for manuscript
def get_num_reviews(manuscript_id):
    connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
    cursor = connection.cursor(buffered=True)

    get_completed_reviews_query = "SELECT * " \
                                  "FROM feedback " \
                                  "WHERE Manuscript_idManuscript = " + str(manuscript_id) + \
                                  " AND recommendation IN ('accept', 'reject')"
    cursor.execute(get_completed_reviews_query)
    num_of_reviews = cursor.rowcount
    cursor.close()
    connection.close()

    return num_of_reviews

# returns true if this issue exists, false else
def issue_exists(issue_year, issue_period_number):
    connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
    cursor = connection.cursor(buffered=True)

    issue_exists_query = "SELECT * " \
                         "FROM issue " \
                         "WHERE publicationYear = '" + issue_year + "-01-01' " \
                         "AND periodNumber = " + issue_period_number
    cursor.execute(issue_exists_query)

    if cursor.rowcount == 1:
        cursor.close()
        connection.close()
        return True

    cursor.close()
    connection.close()

    return False

# returns issue id given the publication year and number
def get_issue_id_from_year_number(issue_year, issue_period_number):
    connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
    cursor = connection.cursor(buffered=True)

    get_issue_id_query = "SELECT idIssue " \
                         "FROM issue " \
                         "WHERE publicationYear = '" + issue_year + "-01-01' " \
                                                                    "AND periodNumber = " + issue_period_number
    cursor.execute(get_issue_id_query)
    issue_id = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return issue_id

# returns number of pages that issue would have if you added the pages in the manuscript specified by manuscript_id to the number of pages already in the issue
def get_num_pages_in_issue(issue_year, issue_period_number, manuscript_id):
    connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
    cursor = connection.cursor(buffered=True)
    issue_id = get_issue_id_from_year_number(issue_year, issue_period_number)

    # 1st sub-query: gets the sum of all pages for manuscripts currently scheduled for the given issue
    # 2nd sub-query: gets number of pages for the proposed manuscript
    # Main Query: gets the sum of pages from the two sub-queries.
    num_pages_query = "SELECT SUM(pages) AS totalPages " \
                      "FROM ( SELECT SUM(pageCount) AS pages " \
                             "FROM acceptedmanuscript AM " \
                             "INNER JOIN manuscript M ON M.idManuscript = AM.Manuscript_idManuscript " \
                             "WHERE issue_idIssue = " + str(issue_id) + " AND M.status = 'scheduled' " \
                             "" \
                             "UNION ALL " \
                             "" \
                             "SELECT pageCount AS pages " \
                             "FROM acceptedManuscript " \
                             "WHERE Manuscript_idManuscript = " + manuscript_id + ") AS P "
    cursor.execute(num_pages_query)

    num_pages = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return num_pages

# returns the number of manuscripts that are scheduled to be in this issue
def get_num_manuscripts_for_issue(issue_year, issue_period_number):
    connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
    cursor = connection.cursor(buffered=True)

    issue_id = get_issue_id_from_year_number(issue_year, issue_period_number)

    get_num_manuscripts_query = "SELECT * " \
                                "FROM acceptedManuscript " \
                                "WHERE Issue_idIssue = " + str(issue_id)
    cursor.execute(get_num_manuscripts_query)

    num_of_manuscripts = cursor.rowcount

    cursor.close()
    connection.close()

    return num_of_manuscripts

# returns true if the manuscript is indeed assigned to the reviewer specified by the id_of_logged_in_user, false else
def manuscript_is_assigned_to_reviewer(manuscript_id, id_of_logged_in_user):
    connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
    cursor = connection.cursor(buffered=True)

    reviewer_manuscript_query = "SELECT * FROM feedback WHERE Reviewer_idReviewer = " + str(id_of_logged_in_user) \
                                + " AND Manuscript_idManuscript = " + str(manuscript_id)
    cursor.execute(reviewer_manuscript_query)

    if cursor.rowcount == 1:
        return True

    return False

# return true if the manuscript is in review as its status, false else
def manuscript_is_in_review(manuscript_id):
    connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
    cursor = connection.cursor(buffered=True)

    # returns a row if manuscript is being reviewed (status = "reviewing")
    find_id_query = "SELECT * " \
                    "FROM manuscript " \
                    "WHERE idManuscript = " + str(manuscript_id) + " AND status = \"reviewing\""
    cursor.execute(find_id_query)

    if cursor.rowcount == 1:
        cursor.close()
        connection.close()
        return True  # manuscript has status "reviewing"

    cursor.close()
    connection.close()

    return False

def validate_ri_codes(ri_codes, num_of_entered_codes):
    connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
    cursor = connection.cursor(buffered=True)
    # Gets number of valid interests:
    num_of_valid_codes = 0
    for code in ri_codes:
        validate_interests_query = "SELECT COUNT(idRICode) FROM ricode WHERE RIValue IN (\"" + code + "\")"
        cursor.execute(validate_interests_query)
        if cursor.fetchone()[0] == 1:
            num_of_valid_codes = num_of_valid_codes + 1

    cursor.close()
    connection.close()

    if num_of_valid_codes == num_of_entered_codes:
        return True

    return False

def manuscript_belongs_to_author(author_id, manuscript_id):
    connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
    cursor = connection.cursor(buffered=True)

    belongs_to_author_query = "SELECT * " \
                              "FROM submit " \
                              "WHERE Author_idAuthor = " + str(author_id) + \
                              " AND Manuscript_idManuscript = " + str(manuscript_id)
    cursor.execute(belongs_to_author_query)

    if cursor.rowcount == 1:
        cursor.close()
        connection.close()
        return True

    cursor.close()
    connection.close()
    return False

########################
# # # Main Program # # #
########################

username = raw_input("ManuscriptManager> Enter your database username (root): ").strip()
password = raw_input("ManuscriptManager> Enter your database password(password): ").strip()
host = raw_input("ManuscriptManager> Enter the host (127.0.0.1): ").strip()
database = raw_input("ManuscriptManager> Enter the database name (mydb): ").strip()

while True:

    command = raw_input("ManuscriptManager> ")

    # # # REGISTER # # #
    if user_code == NOT_LOGGED_IN and command[0:15] == "register editor":

        first_name = raw_input("ManuscriptManager> Enter your first name: ").strip()
        last_name = raw_input("ManuscriptManager> Enter your last name: ").strip()
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

        first_name = raw_input("ManuscriptManager> Enter your first name: ").strip()
        middle_initial = raw_input("ManuscriptManager> Enter your middle initial: ").strip()
        last_name = raw_input("ManuscriptManager> Enter your last name: ").strip()
        email = raw_input("ManuscriptManager> Enter your email: ").strip()
        address = raw_input("ManuscriptManager> Enter your address: ").strip()
        affiliation = raw_input("ManuscriptManager> Enter your affiliation: ").strip()
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

        first_name = raw_input("ManuscriptManager> Enter your first name: ").strip()
        last_name = raw_input("ManuscriptManager> Enter your last name: ").strip()
        middle_initial = raw_input("ManuscriptManager> Enter your middle initial: ").strip()
        affiliation = raw_input("ManuscriptManager> Enter your affiliation: ").strip()
        email = raw_input("ManuscriptManager> Enter your email address: ").strip()
        ri_codes = raw_input("ManuscriptManager> Enter 1 to 3 RICodes separated by the '/' character: ").strip()
        ri_codes_list = ri_codes.split('/')
        num_of_entered_ri_codes = len(ri_codes_list)

        if first_name == "" or last_name == "" or ri_codes == "":
            print("Registration failed. Make sure you enter a value for each field.")

        # Number of entered codes must be less than 4 for reviewer to register
        elif num_of_entered_ri_codes > 3:
            print("Registration failed. Make sure you enter no more than three RI codes.")

        else:
            input_valid = validate_ri_codes(ri_codes_list, num_of_entered_ri_codes)

            if not input_valid:
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
        role = raw_input("ManuscriptManager> Enter your role (editor/reviewer/author): ").strip()
        id = raw_input("ManuscriptManager> Enter your id for log-in: ").strip()

        if role == "" or id == "":
            print("You left one or more required fields blank.")

        if role == "editor" or role == "reviewer" or role == "author":
            connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
            cursor = connection.cursor(buffered=True)
            find_id_query = "SELECT * FROM " + role + " WHERE id" + role + " = " + id
            cursor.execute(find_id_query)

            # If role is valid, check if id is in the table for that role
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
                print("That is not a valid id.")
        else:
            print("That is not a valid role.")

    # # # Author-specific commands # # #
    elif user_code == AUTHOR and command[0:6] == "submit":
        title = raw_input("ManuscriptManager> Enter title of paper: ").strip()
        affiliation = raw_input("ManuscriptManager> Enter your affiliation for this paper: ").strip()
        ri_code = []
        ri_code.append(raw_input("ManuscriptManager> Enter the RICode for this paper: ").strip())
        author2 = raw_input("ManuscriptManager> Enter the second author for this paper (leave blank if no second author): ").strip()
        author3 = raw_input("ManuscriptManager> Enter the third author for this paper (leave blank if no third author): ").strip()
        author4 = raw_input("ManuscriptManager> Enter the fourth author for this paper (leave blank if no fourth author): ").strip()
        filename = raw_input("ManuscriptManager> Enter your paper's filename: ").strip()

        if title == "" or affiliation == "" or ri_code == "" or filename == "":
            print("Submission failed. One or more required fields were left blank.")

        # Checks if file exists in current directory
        elif os.path.isfile(filename) == 0:  # invalid file
            print("Submission failed. The specified file does not exist in your current directory.")

        else:
            ri_code_valid = validate_ri_codes(ri_code, 1)

            if not ri_code_valid:
                print("Submission failed. Invalid RICode.")
            else:
                connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
                cursor = connection.cursor(buffered=True)

                document = open(filename, 'rb').read()

                # Gets RICode id needed for the manuscript insert query below
                get_ricode_ids_query = "SELECT idRICode FROM ricode WHERE RIValue = (\"" + ri_code[0] + "\")"
                cursor.execute(get_ricode_ids_query)
                ri_code_id = cursor.fetchone()[0]

                add_manuscript_query = "INSERT INTO manuscript (title, dateReceived, status, Editor_idEditor, statusModifiedDateTime, RICode_idRICode, document) " \
                                     " VALUES (\"" + title + "\", \"" + str(datetime.date.today()) + "\", \"" \
                                       + "submitted" + "\"," + str(7) + ", \"" + str(datetime.date.today()) + "\"," + str(ri_code_id) + ",\"" + document + "\")"

                cursor.execute(add_manuscript_query, document)
                connection.commit()
                manuscript_id = cursor.lastrowid

                submit_manuscript_query = "INSERT INTO submit VALUES (" + str(id_of_logged_in_user) + "," + str(manuscript_id) + ",1, \"" + affiliation + "\" )"
                cursor.execute(submit_manuscript_query)
                connection.commit()

                print("Submission successful. Your manuscript's id is: " + str(manuscript_id))
                connection.close()

    elif user_code == AUTHOR and command[0:6] == "status":
        status_print(AUTHOR, id_of_logged_in_user)

    elif user_code == AUTHOR and command[0:7] == "retract":
        manuscript_id = raw_input("ManuscriptManager> Enter manuscript ID: ").strip()

        if manuscript_id == "":
            print("Canceled retraction. You did not enter a manuscript ID: ")

        else:
            are_you_sure = raw_input("ManuscriptManager> Are you sure you want to delete this manuscript? (yes/no): ").strip()

            if are_you_sure == "no":
                print("Canceled retraction")

            elif are_you_sure == "yes":
                if id_is_valid(MANUSCRIPT, manuscript_id) == False:
                    print("Invalid manuscript ID.")

                elif manuscript_is_typeset(manuscript_id):
                    print("Manuscript has already been sent for typesetting, or has been published already. Too late!").strip()

                elif manuscript_belongs_to_author(id_of_logged_in_user, manuscript_id) == False:
                    print("This manuscript does not belong to you.")

                else:
                    # delete manuscript
                    connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
                    cursor = connection.cursor(buffered=True)
                    delete_manuscript_query = "DELETE FROM manuscript WHERE idManuscript = " + str(manuscript_id)
                    cursor.execute(delete_manuscript_query)
                    connection.commit()
                    connection.close()
                    print("Successfully deleted manuscript.")
            else:
                print("Invalid response.")

    # # # Editor-specific commands # # #
    elif user_code == EDITOR and command[0:6] == "status":
        status_print(EDITOR, id_of_logged_in_user)

    elif user_code == EDITOR and command[0:6] == "assign":
        manuscript_id = raw_input("ManuscriptManager> Enter manuscript ID: ").strip()
        reviewer_id = raw_input("ManuscriptManager> Enter reviewer ID: ").strip()

        if manuscript_id == "" or reviewer_id == "":
            print("Assignment failed. Please enter information for all fields.")

        elif id_is_valid(MANUSCRIPT, manuscript_id) == False:
            print("Assignment failed. Invalid Manuscript ID")

        elif id_is_valid(REVIEWER, reviewer_id) == False:
            print("Assignment failed. Invalid Reviewer ID")

        else:
            connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
            cursor = connection.cursor(buffered=True)

            add_feedback_record_query = "INSERT INTO feedback values (" + str(manuscript_id) + "," + str(reviewer_id) \
                                        + ", curdate(), 0, 0, 0, 0, null, '')"
            cursor.execute(add_feedback_record_query)
            connection.commit()

            cursor.close()
            connection.close()

            print("Successfully assigned manuscript to reviewer.")

    elif user_code == EDITOR and command[0:6] == "reject":
        manuscript_id = raw_input("ManuscriptManager> Enter manuscript ID: ").strip()
        if manuscript_id == "":
            print("Rejection failed. You didn't enter a manuscript ID.")
        elif id_is_valid(MANUSCRIPT, manuscript_id) == False:
            print("Rejection failed. Manuscript ID is invalid.")
        else:
            connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
            cursor = connection.cursor(buffered=True)

            # Updates the status of the manuscript to 'rejected'
            # The instructions say to also update the timestamp but I added a trigger that does that in the last lab.
            reject_manuscript_query = "UPDATE manuscript " \
                                      "SET status = 'rejected' " \
                                      "WHERE idManuscript = " + str(manuscript_id)
            cursor.execute(reject_manuscript_query)
            connection.commit()

            cursor.close()
            connection.close()

            print("Manuscript successfully rejected.")

    elif user_code == EDITOR and command[0:6] == "accept":
        manuscript_id = raw_input("ManuscriptManager> Enter manuscript ID: ").strip()

        if manuscript_id == "":
            print("Acceptance failed. You didn't enter a manuscript ID.")

        elif id_is_valid(MANUSCRIPT, manuscript_id) == False:
            print("Acceptance failed. Manuscript ID is invalid.")

        elif get_num_reviews(manuscript_id) < 3:
            print("Acceptance failed. This manuscript doesn't yet have the required 3 reviews.")

        else:
            connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
            cursor = connection.cursor(buffered=True)

            # Updates the status of the manuscript to 'accepted'
            # The instructions say to also update the timestamp but I added a trigger that does that in the last lab.
            reject_manuscript_query = "UPDATE manuscript " \
                                      "SET status = 'accepted' " \
                                      "WHERE idManuscript = " + str(manuscript_id)
            cursor.execute(reject_manuscript_query)
            connection.commit()

            cursor.close()
            connection.close()
            print("Manuscript successfully accepted.")

    elif user_code == EDITOR and command[0:7] == "typeset":
        manuscript_id = raw_input("ManuscriptManager> Enter manuscript ID: ").strip()
        pp = raw_input("ManuscriptManager> Enter number of pages: ").strip()

        if manuscript_id == "" or pp == "":
            print("Typeset failed because you left some fields blank.")

        elif id_is_valid(MANUSCRIPT, manuscript_id) == False:
            print("Typeset failed. Manuscript ID is invalid.")

        elif could_be_int(pp) == False or int(pp) < 1:
            print("Invalid number of pages.")

        else:
            connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
            cursor = connection.cursor(buffered=True)

            # Updates the status of the manuscript to 'in typesetting'
            # The instructions say to also update the timestamp but I added a trigger that does that in the last lab.

            typeset_query = "UPDATE manuscript " \
                            "SET status = 'in typesetting' " \
                            "WHERE idManuscript = " + str(manuscript_id)
            cursor.execute(typeset_query)
            connection.commit()

            pp_query = "UPDATE acceptedmanuscript " \
                       "SET pageCount = " + str(pp) + \
                       " WHERE Manuscript_idManuscript = " + str(manuscript_id)

            cursor.execute(pp_query)
            connection.commit()

            cursor.close()
            connection.close()

            print("Typeset successful.")

    elif user_code == EDITOR and command[0:8] == "schedule":
        manuscript_id = raw_input("ManuscriptManager> Enter manuscript ID: ").strip()
        issue_year = raw_input("ManuscriptManager> Enter issue year (4 digits): ").strip()
        issue_period_number = raw_input("ManuscriptManager> Enter issue period number (1/2/3/4): ").strip()

        if manuscript_id == "" or issue_year == "" or issue_period_number == "":
            print("Schedule failed. Required fields left blank.")

        elif id_is_valid(MANUSCRIPT, manuscript_id) == False:
            print("Schedule failed. Invalid manuscript id.")

        elif could_be_int(issue_year) == False:
            print("Schedule failed. Invalid year.")

        elif could_be_int(issue_period_number) == False or int(issue_period_number) > 4 or int(issue_period_number) < 1:
            print("Schedule failed. Invalid period number.")

        elif issue_exists(issue_year, issue_period_number) == False:
            print("Schedule failed. That issue does not exist.")

        elif get_num_pages_in_issue(issue_year, issue_period_number, manuscript_id) > 100:
            print("Schedule failed because issues cannot have more than 100 pages!")

        else:
            connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
            cursor = connection.cursor(buffered=True)

            # Updates the status of the manuscript to 'scheduled'
            schedule_manuscript_query = "UPDATE manuscript " \
                                        "SET status = 'scheduled' " \
                                        "WHERE idManuscript = " + str(manuscript_id)
            cursor.execute(schedule_manuscript_query)
            connection.commit()

            issue_id = get_issue_id_from_year_number(issue_year, issue_period_number)

            update_acceptedmanuscript = "UPDATE acceptedmanuscript " \
                                        "SET Issue_idIssue = " + str(issue_id) + " " \
                                        "WHERE Manuscript_idManuscript = " + manuscript_id
            cursor.execute(update_acceptedmanuscript)
            connection.commit()

            cursor.close()
            connection.close()

            print("Manuscript successfully scheduled.")

    elif user_code == EDITOR and command[0:7] == "publish":
        issue_year = raw_input("ManuscriptManager> Enter issue year: ").strip()
        issue_period_number = raw_input("ManuscriptManager> Enter issue period number: ").strip()

        if issue_year == "" or issue_period_number == "":
            print("Publish failed. Required fields left blank.")

        elif could_be_int(issue_year) == False:
            print("Publish failed. Invalid year.")

        elif could_be_int(issue_period_number) == False or int(issue_period_number) > 4 or int(issue_period_number) < 1:
            print("Publish failed. Invalid period number.")

        elif issue_exists(issue_year, issue_period_number) == False:
            print("Publish failed. That issue does not exist.")

        elif get_num_manuscripts_for_issue(issue_year, issue_period_number) < 1:
            print("Publish failed. There are no manuscripts scheduled for this issue.")

        else:
            connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
            cursor = connection.cursor(buffered=True)

            issue_id = get_issue_id_from_year_number(issue_year, issue_period_number)
            # Changes status of manuscripts in given issue to 'published'
            publish_manuscripts_query = "UPDATE manuscript M " \
                                        "INNER JOIN acceptedmanuscript AM ON AM.Manuscript_idManuscript = M.idManuscript " \
                                        "SET status = 'published' " \
                                        "WHERE AM.Issue_idIssue = " + str(issue_id) + " AND M.status = 'scheduled'"
            cursor.execute(publish_manuscripts_query)
            connection.commit()

            update_publication_date_query = "UPDATE issue " \
                                            "SET printDate = curdate() " \
                                            "WHERE idIssue = " + str(issue_id)

            cursor.execute(update_publication_date_query)
            connection.commit()

            cursor.close()
            connection.close()

            print("Publish succeeded.")

    # # # Reviewer-specific commands # # #
    elif user_code == REVIEWER and command[0:6] == "resign":
        id = raw_input("ManuscriptManager> Enter your reviewer id: ").strip()

        if id == "":
            print("You didn't enter an id.")

        elif id_is_valid(REVIEWER, id) == False:
            print("Invalid id.")

        else:
            connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
            cursor = connection.cursor()
            query = "DELETE FROM reviewer WHERE idReviewer = " + str(id_of_logged_in_user)
            cursor.execute(query)
            connection.commit()
            cursor.close()
            connection.close()
            print("Thank you for your service.")

    elif user_code == REVIEWER and command[0:6] == "review":
        manuscript_id = raw_input("ManuscriptManager> Enter manuscript ID: ").strip()
        accept_or_reject = raw_input("ManuscriptManager> What's your recommendation? (accept/reject): ").strip()
        appropriateness = raw_input("ManuscriptManager> Appropriateness rating (1 = low, 10 = high): ").strip()
        clarity = raw_input("ManuscriptManager> Clarity rating (1 = low, 10 = high): ").strip()
        methodology = raw_input("ManuscriptManager> Methodology rating (1 = low, 10 = high): ").strip()
        contribution = raw_input("ManuscriptManager> Contribution to field rating (1 = low, 10 = high): ").strip()

        if manuscript_id == "" or accept_or_reject == "" or appropriateness == "" or clarity == "" or methodology == "" or contribution == "":
            print("Review failed. Required fields left blank.")

        elif id_is_valid(MANUSCRIPT, manuscript_id) == False:
            print("Review failed. Invalid manuscript id.")

        elif could_be_int(appropriateness) == False or could_be_int(clarity) == False or could_be_int(methodology) == False or could_be_int(contribution) == False \
            or int(appropriateness) < 1 or int(appropriateness) > 10 or int(clarity) < 1 or int(clarity) > 10 or int(methodology) < 1 or int(methodology) > 10 \
            or int(contribution) < 1 or int(contribution) > 10:
            print("One or more invalid ratings. Ratings must be a number between 1 and 10, inclusive.")

        elif manuscript_is_assigned_to_reviewer(manuscript_id, id_of_logged_in_user) == False:
            print("Review failed. You are not a reviewer for this manuscript.")

        elif manuscript_is_in_review(manuscript_id) == False:
            print("Review failed. This manuscript is not currently in review.")

        elif accept_or_reject == "accept" or accept_or_reject == "reject":
            connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
            cursor = connection.cursor(buffered=True)
            # Gets number of valid interests:

            validate_interests_query = "UPDATE feedback " \
                                       "SET appropriateRating = " + str(appropriateness) + ", " \
                                       "    clarityRating = " + str(clarity) + ", " \
                                       "    methodologyRating =  " + str(methodology) + ", " \
                                       "    contributionRating =  " + str(contribution) + ", " \
                                       "    dateFeedbackReceived = curdate(),  "\
                                       "    recommendation = \"" + accept_or_reject + "\"" \
                                       " WHERE Manuscript_idManuscript = " + str(manuscript_id) + \
                                       " AND Reviewer_idReviewer = " + str(id_of_logged_in_user)
            cursor.execute(validate_interests_query)
            connection.commit()
            cursor.close()
            connection.close()

            print("Thank you for your review!")

        else:
            print("Invalid recommendation (must be 'accept' or 'reject').")

    elif user_code == REVIEWER and command[0:6] == "status":
        status_print(REVIEWER, id_of_logged_in_user)

    elif command[0:6] == "logout":
        user_code = NOT_LOGGED_IN
    # # # help command # # #
    elif command[0:4] == "help":
        print("Welcome to ManuscriptManager\n\n")
        print("General Commands:\n")
        print("register editor")
        print("register author")
        print("register reviewer")
        print("login\n")
        print("logout\n")
        print("Commands for authors:\n")
        print("submit - submit a manuscript")
        print("status - see the statuses of your manuscripts")
        print("retract - retract a manuscript\n")
        print("Commands for editors:\n")
        print("status - see the status of your manuscripts")
        print("assign - assign a manuscript to a reviewer")
        print("reject - reject a manuscript")
        print("accept - accept a manuscript")
        print("typeset - typeset a manuscript")
        print("schedule - schedule a manuscript to appear in an issue")
        print("publish - publish an issue\n")
        print("Commands for reviewers\n")
        print("resign - stop being a reviewer")
        print("review - review a manuscript")
        print("status - see the status of your manuscripts")

    else:
        print("Invalid command.")
