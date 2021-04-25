import random
import validations


def init():
    print("Welcome to bankPYTHON")

    have_account = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print("You have selected invalid option")
        init()


database = {}


def login():
    print(" ----- Log in to your account  -----")

    is_login_successful = False

    while is_login_successful == False:
        account_number_from_user = input("What is your account number? \n")
        account_number_from_user = validations.account_number_validation(account_number_from_user)

        if account_number_from_user:
            password = input("What is your password? \n")
            for accountNumber, userDetail in database.items():
                if accountNumber == int(account_number_from_user) and userDetail[3] == password:
                    is_login_successful = True
                    bank_operations(userDetail)

            print('Invalid account or password')


def register():
    print(" ------- Register -------- ")
    email = input("Please input your email address: ")
    first_name = input("What is your first name: ")
    last_name = input("What is your last name: ")
    password = input("Create a password for yourself: ")
    account_balance = 0

    account_number = generate_account_number()
    print("Your account has been successfully created")
    print(f"Dear {first_name}, your account number is {account_number}. Do keep it safe")

    database[account_number] = [first_name, last_name, email, password, account_balance]

    login()


def bank_operations(user):
    print(f"Welcome {user[0]} {user[1]}")

    right_option = True

    while right_option == True:
        selected_option = int(input("What would you like to do (1) Deposit (2) Withdrawal (3) Logout (4) Exit: "))
        if selected_option == 1:
            right_option = False
            deposit_operation(user)
        elif selected_option == 2:
            right_option = False
            withdrawal_operation(user)
        elif selected_option == 3:
            right_option = False
            login()
        elif selected_option == 4:
            exit()
        else:
            print("Invalid option selected")


def withdrawal_operation(user):
    withdrawal_amount = input("How much will you like to withdraw: \n")

    stay_withdrawing = True
    while stay_withdrawing:
        if withdrawal_amount < user[4]:
            user[4] = user[4] - withdrawal_amount
            print(f"Please take your cash: #{withdrawal_amount}")
            print(f"Your remaining balance is {user[4]} \n \n")
        else:
            print("You sure know it's not right to desire to reap what you didn't sow. We don't do giveaway here")
            stay_withdrawing = False


def deposit_operation(user):
    deposit_amount = input("How much will you like to deposit: \n")
    user[4] = user[4] + deposit_amount
    print(f"You just deposited #{deposit_amount} successfully.")
    print(f"Your remaining balance is {user[4]} \n \n")


def generate_account_number():
    return random.randrange(111111111, 5555555559)


def get_user_current_balance(user_details):
    return user_details[4]
    print("Current Balance")


init()
