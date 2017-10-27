Anja Subasic and Marissa Le Coz
Lab 2d
README

How to run the program:

From the command line, do `python app.py`. This will launch the "ManuscriptManager>" prompt.

You will be asked for your database login, database password, database host, and database name to use in your connections to the database.
(Defaults that we used are given in parentheses.)

For a list of commands, type the `help` command.

When submitting a document, you can use manuscript.txt, which we've included for your convenience.

Assumptions:
- We assume that the issue table is already populated in the database. (The assignment page doesn't specify any sort of command
  for "creating" and issue, only adding manuscripts to an issue.) In our provided sql code, we have populated the issue table: we have included
  issues 1-4 from 2014 to 2017.
- We assume that a reviewer can only resign once s/he is logged in. The assignment page seemed to imply that this command could
  be run without logging in, but we didn't think that made much sense.
- We assume we shouldn't allow authors to retract manuscripts that are scheduled and published, in addition to 'in typesetting' 
  status mentioned in the requirements.
- If you're already logged in, you can't login again. You must first use the logout command. (So, in order to switch roles (i.e., editor,
  author, reviewer), you need to log out and then log back in as the new role.)
- An editor must accept a manuscript before typesetting it.

Our test cases:
- Please see test_cases.txt for the cases we used to test our app.
