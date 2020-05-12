# snbank
 Replica/Immitation  of Banking system

Code Setup:
 *Install python 3 on system
  run code using an IDE (e.g Pycharm, VS codes, etc)
  code can also be run on the terminal (make sure all related files are in the same directory).*

Code features
The code consits of six functions:

home_page function:
	*This asks the user to eithe login as a staff, or close the program*

login function:
	*This function collects the staff details and compares with the staff records in staff.txt to verify for successful login.
	After a successful login, a new file (session.txt) is created which record all activities carried out by the staff while logged in. The session purpose function is then called.*

session_purpose function:
	*This function asks the staff the purpose for logging in, i.e if to create a new bank account or to check the details of an existing account or or if to logout.
	when the choice is entered, the corresponding funtion is called.*

create_account funtion
	 *Here the customer details are collected, account name, opening amount, account type, accounbt email, etc. After collection a new account number starting with 150... is generated. 
	 After successful account creation, the details of the new*

check_account function:
	*This collects an account number, then checks if it exists in the customer.txt file. if it does it prints ount the details of the cusromer it belongs to.*

the logout function whn called deletes the session.txt file and returns the program to the home_page.
