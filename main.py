from random import randint
from textwrap import dedent
from datetime import datetime

time_stamp = datetime.now(tz=None)


def session_purpose(username, session_log):
    accounts = {
        "1": "Current Account",
        "2": "Savings account",
        "3": "Recurring Deposit Account",
        "4": "Fixed Deposit Account"
    }

    activity = input("1. Create a new bank account\n2. Check Account details\n3. Logout\nType in option: ")
    if activity == "1":
        acc_name = input("Enter Account Name: ")
        while True:
            try:  # to check if input is an integer
                opening_balance = int(input("Enter Opening balance (In figures): "))
                break
            except ValueError:
                print("Enter an amount in figures")
        print(dedent("""
                1. Current Account
                2. Savings account
                3. Recurring Deposit Account
                4. Fixed Deposit Account"""))
        while True:
            acc_type = input("Type in Option (1, 2, 3 or 4): ")
            if "1" or "2" or "3" or "4" in acc_type:
                acc_type = accounts.get(acc_type)  # to get the account name from accounts dict
                break
            else:
                print("Choose the correct option")
        acc_email = input("Enter Account Email: ")
        num_list = [1, 5, 0]
        for x in range(7):
            num_list.append(randint(0, 9))
        num_list = [str(x) for x in num_list]  # converts all integers to string for joining
        acc_number = "".join(num_list)
        print(f"Account number: {acc_number}")

        customer_details = acc_name, opening_balance, acc_type, acc_email, acc_number
        customer_file = open("customer", 'a+')
        customer_file.write(f"{str(customer_details)}\n")  # writes all the customer details into to the customer file
        session_log.write(f"{time_stamp}: @{username} Created a new {acc_type} account\n")

        session_purpose(username, session_log)

    elif activity == "2":
        customer_details = open("customer", "r").read()
        print(customer_details)
        session_purpose(username, session_log)

    elif activity == "3":
        session_log.write(f"{time_stamp}: @{username} logged out\n")
        # remove("session")
        home_page()


def login():
    while True:
        username = input("Enter Username: ")
        password = input("Enter password: ")
        staff_log = open("staff").read()
        staff_list = staff_log.splitlines()

        new_list = []
        for staff in staff_list:
            new_list.append(staff.split())

        logged = False
        count = 0
        for staff in new_list:
            count += 1
            if username == staff[0] and password == staff[1]:
                logged = True
                session_log = open("session", "w+")
                session_log.write(f"{time_stamp}: @{username} logged in\n")
                session_log = open("session", "a+")
                session_purpose(username, session_log)
            if logged is False and count == len(new_list):
                print("Unauthorised login!\nYou are not a staff\n")


def home_page():
    start_choice = input("1. Login\n2. Close App\nType in option: ")
    while True:
        if start_choice == "1":
            login()
        elif start_choice == "2":
            exit(0)
        else:
            print("Enter a valid option!")


print("Welcome to SN Bank")
home_page()
