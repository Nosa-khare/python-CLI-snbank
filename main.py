import json
from os import remove
from random import randint
from textwrap import dedent
from datetime import datetime

time_stamp = datetime.now(tz=None)


def logout(username):
    with open("session.txt", "a+") as session_log:
        session_log.write(f"{time_stamp}: @{username} logged out")
        print("\n")
    remove("session.txt")
    home_page()


def check_account_details(username):
    acc_num = input("\nEnter account number for verification: ")
    customer_file = open("customer.txt", "r").read()
    customer_list = customer_file.splitlines()  # split each lines of the file into a list

    found = False
    counter = 1
    for item in customer_list:
        details = json.loads(item)  # converts the string dictionary in to a python dictionary object
        if acc_num == details["Account number"]:  # checks if the account number exits in any of the dicts
            print(details)
            found = True
        if counter == len(customer_list) and not found:  # if all dictionaries has been looped through and not found
            print(f"No record of account with Account Number: {acc_num} found")
        counter += 1

    with open("session.txt", "a+") as session_log:
        session_log.write(f"{time_stamp}: @{username} checked account details")
        session_log.write("\n")

    session_purpose(username)


def create_account(username):

    accounts = {
        "1": "Current Account",
        "2": "Savings account",
        "3": "Recurring Deposit Account",
        "4": "Fixed Deposit Account"
    }
    # to get an account name
    acc_name = input("\nEnter Account Name: ")

    # deposit an opening balance
    while True:
        try:
            opening_balance = int(input("Enter Opening balance (In figures): "))
            break
        except ValueError:
            print("Enter an amount in figures")

    # to select an account type
    while True:
        acc_type = input(dedent("""
                                Choose an account type
                                1. Current Account
                                2. Savings account
                                3. Recurring Deposit Account
                                4. Fixed Deposit Account
                                (1, 2, 3, 4): """))
        if acc_type in ["1", "2", "3", "4"]:
            acc_type = accounts.get(acc_type)  # to set account type to the corresponding name from accounts dict
            break
        else:
            print("Choose an account type")

    # getting an account email
    acc_email = input("\nEnter Account Email: ")

    # generating an account number
    num_list = [1, 5, 0]  # to enable every generated acc number start with 150
    [num_list.append(randint(0, 9)) for x in range(7)]
    acc_number = "".join([str(x) for x in num_list])  # converts all integers to strings and joins
    print(f"Account number: {acc_number}")

    customer_details = {"Account name": acc_name,
                        "Account number": acc_number,
                        "Account balance": f"${opening_balance}",
                        "Account type": acc_type,
                        "Account email": acc_email
                        }

    # adding the dictionary of the new account created to the customer txt file
    customer_file = open("customer.txt", 'a')
    customer_file.write(json.dumps(customer_details))  # writes customer_details as a dict into customer file
    customer_file.write("\n")
    customer_file.close()

    with open("session.txt", "a+") as session_log:
        session_log.write(f"{time_stamp}: @{username} Created a new {acc_type} account")
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
    staff_log = open("staff.txt").read()  # open staff.txt file for reading
    staff_list = staff_log.splitlines()  # split each lines of the file into a list

    new_list = []
    for staff in staff_list:
        new_list.append(staff.split())

    logged = False
    count = 1
    for staff in new_list:
        if username == staff[0] and password == staff[1]:
            logged = True
            with open("session.txt", "w") as session_log:
                session_log.write(f"{time_stamp}: @{username} logged in\n")

            session_purpose(username)

        if not logged and count == len(new_list):
            print("Unauthorised login!\nYou are not a staff")
            login()
        count += 1


def home_page():
    start_choice = input("1. Login\n2. Close App\nType in option: ")
    if start_choice == "1":
        login()
    elif start_choice == "2":
        exit(0)
    else:
        print("Enter a valid option!")
        home_page()


print("Welcome to SN Bank")
home_page()
