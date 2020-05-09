import json
from os import remove
from random import randint
from textwrap import dedent
from datetime import datetime

time_stamp = datetime.now(tz=None)


def logout(username):
    session_log = open("session.txt", "a+")
    session_log.write(f"{time_stamp}: @{username} logged out\n")
    session_log.close()
    remove("session.txt")
    home_page()


def check_account_details(username):
    acc_num = input("\nEnter account number for verification: ")
    customer_file = open("customer.txt", "r").read()
    customer_list = customer_file.splitlines()

    found = False
    counter = 1
    for item in customer_list:
        details = json.loads(item)
        if acc_num == details["Account number"]:
            print(details)
            found = True
        if counter == len(customer_list) and not found:
            print(f"No record of account with Account Number: {acc_num} found")
        counter += 1

    session_log = open("session.txt", "a+")
    session_log.write(f"{time_stamp}: @{username} checked account details")
    session_log.write("\n")
    session_log.close()
    session_purpose(username)


def create_account(username):

    accounts = {
        "1": "Current Account",
        "2": "Savings account",
        "3": "Recurring Deposit Account",
        "4": "Fixed Deposit Account"
    }

    acc_name = input("\nEnter Account Name: ")
    while True:
        try:  # to check if input is an integer
            opening_balance = int(input("Enter Opening balance (In figures): "))
            break
        except ValueError:
            print("Enter an amount in figures")

    while True:
        acc_type = input(dedent("""
                                Choose an account type
                                1. Current Account
                                2. Savings account
                                3. Recurring Deposit Account
                                4. Fixed Deposit Account
                                (1, 2, 3, 4): """))
        if "1" == acc_type or "2" == acc_type or "3" == acc_type or "4" == acc_type:
            acc_type = accounts.get(acc_type)  # to get the account name from accounts dict
            break
        else:
            print("Choose an account type")

    acc_email = input("\nEnter Account Email: ")

    num_list = [1, 5, 0]
    for x in range(7):
        num_list.append(randint(0, 9))
    num_list = [str(x) for x in num_list]  # converts all integers to string for joining
    acc_number = "".join(num_list)
    print(f"Account number: {acc_number}")

    customer_details = {"Account name": acc_name, "Account number": acc_number,
                        "Account balance": f"${opening_balance}", "Account type": acc_type,
                        "Account email": acc_email}

    customer_file = open("customer.txt", 'a')
    customer_file.write(json.dumps(customer_details))  # writes customer_details as a dict into customer file
    customer_file.write("\n")
    customer_file.close()

    session_log = open("session.txt", "a+")
    session_log.write(f"{time_stamp}: @{username} Created a new {acc_type} account")
    session_log.write("\n")
    session_log.close()  # close session file in order to save changes in runtime

    session_purpose(username)


def session_purpose(username):
    while True:
        activity = input("\n1. Create a new bank account\n2. Check Account details\n3. Logout\nType in option: ")

        if activity == "1":
            create_account(username)

        elif activity == "2":
            check_account_details(username)

        elif activity == "3":
            logout(username)
        else:
            print("Invalid")


def login():
    while True:
        username = input("\nEnter Username: ")
        password = input("Enter password: ")
        staff_log = open("staff.txt").read()
        staff_list = staff_log.splitlines()

        new_list = []
        for staff in staff_list:
            new_list.append(staff.split())

        logged = False
        count = 1
        for staff in new_list:
            if username == staff[0] and password == staff[1]:
                logged = True
                session_log = open("session.txt", "w")
                session_log.write(f"{time_stamp}: @{username} logged in\n")
                session_log.close()
                session_purpose(username)

            if logged is False and count == len(new_list):
                print("Unauthorised login!\nYou are not a staff")
            count += 1


def home_page():
    while True:
        start_choice = input("1. Login\n2. Close App\nType in option: ")
        if start_choice == "1":
            login()
        elif start_choice == "2":
            exit(0)
        else:
            print("Enter a valid option!")


print("Welcome to SN Bank")
home_page()
