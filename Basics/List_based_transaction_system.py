balance = 0
transactions = []
password = 'RCB12@@1'

def validate_password(p):
    return p == password

def take_pass():
    return input("Enter your password: ")

def deposit():
    global balance
    try:
        amt = int(input("Enter Deposit Amount: "))
        if amt <= 0:
            print("Enter valid amount")
            return
        balance += amt
        transactions.append("Deposit: " + str(amt))
        print("Amount credited successfully")
    except:
        print("Invalid input")

def withdraw():
    global balance
    try:
        amt = int(input("Enter Withdraw Amount: "))
        if amt <= 0:
            print("Enter valid amount")
            return
        if balance < amt:
            print("Not enough balance")
        else:
            balance -= amt
            transactions.append("Withdraw: " + str(amt))
            print("Amount debited successfully")
    except:
        print("Invalid input")

def print_transactions():
    print("\nTransaction History:")
    if not transactions:
        print("No transactions yet")
    else:
        for t in transactions:
            print(t)

while True:
    input_pass = take_pass()

    if validate_password(input_pass):
        print("\nWelcome! Choose an option:")
        print("0. Reset Password")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid input")
            continue

        if choice == 0:
            old = take_pass()
            if validate_password(old):
                password = input("Enter new password: ")
                print("Password updated")
            else:
                print("Wrong password")
        elif choice == 1:
            deposit()
        elif choice == 2:
            withdraw()
        elif choice == 3:
            print("Available Balance:", balance)
        elif choice == 4:
            print_transactions()
        elif choice == 5:
            print("Thanks for using the system")
            break
        else:
            print("Invalid choice")

    else:
        print("Wrong password\n")
