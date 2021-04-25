def account_number_validation(account_number):
    if account_number:
        if len(str(account_number)) == 10:
            try:
                int(account_number)
                return True
            except ValueError:
                print("Invalid account number. Input only integers for account number")
                return False
        else:
            print("Account number must be exactly 10 digits")
            return False
    else:
        print("Account number is required")
        return False
