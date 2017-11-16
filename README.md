# Manuscript Manager

Manuscript Manager is a project built for a Database Systems class at Dartmouth College (Fall 2017) in collaboration with Marissa Le Coz.

## Project Structure
Project was implemented in Python 2.7, in a single .py file (as required), using a MySQL database.

## Project Requirements:

### Domain description (based on a question from Coronel 12th ed., Chapter 5):
The domain that you will model in this assignment is that of an academic journal’s manuscript management system. You are to create a system to support the business needs described below.

The Journal of E-commerce Research Knowledge is a prestigious information systems research journal. It uses a peer-review process to select manuscripts for publication. Only about 10 percent of the manuscripts submitted to the journal are accepted for publication. A new issue of the journal is published each quarter.

Unsolicited manuscripts are submitted by authors. When a manuscript is received, the editor will assign the manuscript a number, and record some basic information about it in the system. The title of the manuscript, the date it was received, and a manuscript status of “received” are entered. Information about the author(s) is also recorded. For each author, the author’s name, mailing address, and e-mail address is recorded. In addition, the primary author's current affiliation (school or company for which the author works) is also recorded. Every manuscript must have at least one author. Only authors that have submitted manuscripts are kept in the system. It is typical for a manuscript to have several authors. A single author may have submitted many different manuscripts to the journal. Additionally, when a manuscript has multiple authors, it is important to record the order in which the authors are listed in the manuscript credits.

At her earliest convenience, the editor will briefly review the topic of the manuscript to ensure that the manuscript’s contents fall within the scope of the journal. If the content is not within the scope of the journal, the manuscript’s status is changed to “rejected” and the author is notified via e-mail. If the content is within the scope of the journal, then the editor selects three or more reviewers to review the manuscript.

Reviewers work for other companies or universities and read manuscripts to ensure the scientific validity of the manuscripts. For each reviewer, the system records a reviewer number, reviewer name, reviewer e-mail address, affiliation, and areas of interest. Areas of interest are pre-defined areas of expertise that the reviewer has specified. An area of interest is identified by a Reviewer Interest Code (or RICode, defined here). A reviewer can have up to three areas of interest, and an area of interest can be associated with many reviewers. All reviewers must specify at least one area of interest.

The editor will change the status of the manuscript to “under review” and record which reviewers the manuscript was sent to and the date on which it was sent to each reviewer. A reviewer will typically receive several manuscripts to review each year, although new reviewers may not have received any manuscripts yet.

The reviewers will read the manuscript at their earliest convenience and provide feedback to the editor regarding the manuscript. The feedback from each reviewer includes rating the manuscript on a 10-point scale for appropriateness, clarity, methodology, and contribution to the field, as well as a recommendation for publication (accept or reject). The editor will record all of this information in the system for each review received from each reviewer and the date that the feedback was received. Once all of the reviewers have provided their evaluation of the manuscript, the editor will decide whether or not to publish the manuscript. If the editor decides to publish the manuscript, the manuscript’s status is changed to “accepted” and the date of acceptance for the manuscript is recorded. If the manuscript is not to be published, the status is changed to “rejected.”

Once a manuscript has been accepted for publication, it must be scheduled. For each issue of the journal, the publication year and publication period number ( 1 (Winter), 2 (Spring), 3 (Summer), 4 (Fall) ) are recorded. An issue will contain many manuscripts, although the issue may be created in the system before it is known which manuscripts will go in that issue. For cost reasons, each issue is limited to 100 pages of manuscripts. An accepted manuscript appears in only one issue of the journal. Each manuscript goes through a typesetting process that formats the content (font, font size, line spacing, justification, etc.). Once the manuscript has been typeset, the number of pages that the manuscript will occupy is recorded in the system. The editor will then make decisions about which issue each accepted manuscript will appear in and the order of manuscripts within each issue. The order and the beginning page number for each manuscript must be stored in the system. Once the manuscript has been scheduled for an issue, the status of the manuscript is changed to “scheduled.” Once an issue is published, the print date for the issue is recorded, and the statuses of all of the manuscripts in that issue are changed to “published.”

### System Specification
You will design and implement a database for the above domain, and a front end application intended for authors, editors, and reviewers:

Formally, your application should provide the following three roles.
The mode may be determined either by the first command the user enters:

the register command, which specifies author, editor, or `reviewer
the login command, which specifies the unique <id> assigned to the person which defines the role.
The three modes are defined as follows:

Author:
REGISTER a new Author
register author <fname> <lname> <email> <address> <affiliation>
store the information along with a unique id
LOGIN
login <id> Upon entering his/her unique id (no fancy userid/password stuff), the system should display a greeting followed by:
The Author’s full name and address, followed by the output from the status command (when executed by an Author): # submitted, # under review, # rejected, # accepted, # in typesetting, # scheduled for publication, # published

The Author may then:
submit <title> <Affiliation> <RICode> <author2> <author3> <author4> <filename>
providing title, the author's current affiliation (a string), RICode representing the subject area, optional additional authors, and the document itself (as a SQL BLOB).
the system returns confirmation with a system-wide unique manuscript id, creates a new manuscript tuple with that id, a status of “submitted”, and a SUBMITTED timestamp
the submitting author becomes the primary author, by definition.
each submitted manuscript has exactly one RICode.
co-authors need not be registered and no information is kept about them (other than their names, as indicated above)
STATUS produces a report of all the author’s manuscripts currently in the system where he/she is the primary author. Only the most recent status timesstamp is kept and reported.
RETRACT a manuscript, which, after a “are you sure?” prompt gets a “Yes”, immediately removes the manuscript from the system as long as it has not been sent for typesetting.
Editor
REGISTER a new Editor
register editor <fname> <lname>
store the first name,last name, and a unique id which will be the editor_id for that editor.
there are one or more editors, but only one editor will handle a specific manuscript. You do not need to handle an “editor in chief” role.
LOGIN
login <editor_id> Upon entering his/her unique id (no fancy userid/password stuff), the system should display a greeting followed by:
The Editor’s full name and the output from the STATUS command: # submitted, # under review, # rejected, # accepted, # in typesetting, # scheduled for publication, # published

The Editor may then query or set the status of manuscripts in the system using these commands:

status lists all manuscripts in the system sorted by status and then <manu#>.
assign <manu#> <reviewer id> assigns a manuscript to a reviewer and sets its status to “Reviewing” with a timestamp.
reject <manu#> sets the manuscript’s status to “Rejected” with a timestamp
accept <manu#> sets a manuscript’s status to “Accepted” with a timestamp. Note that this should ONLY be allowed if the manuscript has three completed reviews.
typeset <manu#> <pp> sets a manuscript’s status to “Typeset” and the number of pages (pp) are stored. No status change is necessary since the number of pages was unknown prior to typesetting.
schedule <manu#> <issue> an Accepted manuscript is set to appear in a specific unpublished issue <issue> and its status set to “Scheduled”. If the addition of this manuscript to the issue would cause the issue to exceed 100 pages the “schedule” request should fail.
publish <issue> an issue that has manuscripts assigned to it is sent to be printed. If the issue has at least one manuscript scheduled for it, record the timestamp of the decision and set all its manuscript(s) status as “Published”.
Reviewer
REGISTER a new Reviewer
Collecting first name, last name, and at least one but not more than three valid RICodes.
Provide the Reviewer with a system-wide unique id
Create a new reviewer in the system with all of this info.
RESIGN
Upon entering his/her unique id (no fancy userid/password stuff), the system should display a greeting and remove that reviewer from the system, followed by:
Thank you for your service.
LOGIN
Upon entering his/her unique id (no fancy userid/password stuff), the system should display a greeting followed by:
The Reviewer’s full name and the output from the STATUS command LIMITED to manuscripts assigned to that reviewer. Only the most recent status timesstamp is kept and reported.
The Reviewer may then set the status of his/her assigned manuscripts in the system:
REVIEW-REJECT a manuscript with four scores (1=low, 10=high) for appropriateness, clarity, methodology, and contribution to the field.
REVIEW-ACCEPT a manuscript with four scores (1=low, 10=high) for appropriateness, clarity, methodology, and contribution to the field.
Any attempts to act on a manuscript not assigned to this reviewer or a manuscript not in “Reviewing” status should fail with an appropriate message.
An individual may only have one of the above three roles.

No GUI interface is required. Your application should accept its input (commands) via stdin. The testing that the TA’s will do to assess each part of Lab2 will be via stdin. All other input interfaces (e.g., command-line options, GUI’s, etc.) are optional.

You may implement this using Python, Java, or Javascript/Typescript only.
