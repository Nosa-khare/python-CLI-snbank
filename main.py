import json
from os import remove
from random import randint
from textwrap import dedent
from datetime import datetime

time_date_stamp = datetime.now(tz=None)


def logout(username):
    with open("session.txt", "a+") as session_log:
        session_log.write(f"{time_date_stamp}: @{username} logged out")
        print("\n")
    remove("session.txt")

    home_page()  # return to home page


def check_account_details(username):
    account_number = input("\nEnter account number for verification: ")

    customer_file = open("customer.txt", "r").read()
    customer_list = customer_file.splitlines()  # split each lines of the file into a list

    found = False
    counter = 1  # representing how many items in the list the for loop has checked
    for item in customer_list:

        details = json.loads(item)  # converts the string dictionary in to a python dictionary object

        if account_number == details["Account number"]:  # checks if the account number exits in any of the dicts
            print(details)
            found = True
            with open("session.txt", "a+") as session_log:  # opens session.txt in append mode
                session_log.write(  # code continues in next line
                    f"{time_date_stamp}: @{username} checked {details.get('Account number')} account details")
                session_log.write("\n")

        if counter == len(customer_list) and not found:  # if all dictionaries has been looped through and not found
            print(f"No record of account with Account Number: {account_number} found")
            with open("session.txt", "a+") as session_log:
                session_log.write(  # continue in next line
                    f"{time_date_stamp}: @{username} checked for an unregistered account")
                session_log.write("\n")
        counter += 1

    session_purpose(username)


def create_account(username):

    accounts_dict = {
        "1": "Current Account",
        "2": "Savings account",
        "3": "Recurring Deposit Account",
        "4": "Fixed Deposit Account"
    }
    # to get an account name
    account_name = input("\nEnter Account Name: ")

    # deposit an opening balance
    while True:
        try:
            opening_balance = int(input("Enter Opening balance (In figures): "))
            break
        except ValueError:
            print("Enter an amount in figures")

    # to select an account type
    while True:
        account_type = input(dedent("""
                                Choose an account type
                                1. Current Account
                                2. Savings account
                                3. Recurring Deposit Account
                                4. Fixed Deposit Account
                                (1, 2, 3, 4): """))
        if account_type in ["1", "2", "3", "4"]:
            account_type = accounts_dict.get(account_type)  # set account type to corresponding name from accounts dict
            break
        else:
            print("Choose an account type")

    # getting an account email
    account_email = input("\nEnter Account Email: ")

    # generating an account number
    number_list = [1, 5, 0]  # to enable every generated acc number start with 150
    [number_list.append(randint(0, 9)) for x in range(7)]
    account_number = "".join([str(i) for i in number_list])  # converts all integers to strings and joins
    print(f"Account number: {account_number}")

    customer_details = {"Account name": account_name,
                        "Account number": account_number,
                        "Account balance": f"${opening_balance}",
                        "Account type": account_type,
                        "Account email": account_email
                        }

    # adding the dictionary of the new account created to the customer txt file
    customer_file = open("customer.txt", 'a')
    customer_file.write(json.dumps(customer_details))  # writes customer_details as a dict into customer file
    customer_file.write("\n")
    customer_file.close()

    with open("session.txt", "a+") as session_log:
        session_log.write(f"{time_date_stamp}: @{username} Created a new {account_type}")
        session_log.write("\n")

    session_purpose(username)


def session_purpose(username):
    activity = input(dedent("""
                    1. Create a new bank account
                    2. Check Account details
                    3. Logout
                    Type in option: """))
    if activity == "1":
        create_account(username)

    elif activity == "2":
        check_account_details(username)

    elif activity == "3":
        logout(username)
    else:
        print("Invalid")
        session_purpose(username)


def login():
    username = input("\nEnter Username: ")
    password = input("Enter password: ")
    staff_file = open("staff.txt").read()  # open staff.txt file for reading
    staff_list = staff_file.splitlines()  # split each lines of the file into a list

    new_list = []
    for staff in staff_list:
        new_list.append(staff.split())  # each item of the staff_list is appended as a list into new_list
        # new_list is no a list of lists, where y each inner list contains the details of a staff as items

    logged = False
    counter = 1  # to represent the number of list(s) the for loop has checked
    for staff in new_list:
        if username == staff[0] and password == staff[1]:
            logged = True
            with open("session.txt", "w") as session_log:
                session_log.write(f"{time_date_stamp}: @{username} logged in\n")
            session_purpose(username)  # after login is successful head to session_purpose page

        if not logged and counter == len(new_list):
            print("Unauthorised login!\nYou are not a staff")
            login()
        counter += 1  # increment


def home_page():
    start_choice = input("1. Login\n2. Close App\nType in option: ")
    if start_choice == "1":
        login()
    elif start_choice == "2":
        exit(0)
    else:
        print("Enter a valid option!")
        home_page()


# PROGRAM STARTS
print("Welcome to SN Bank")
home_page()
