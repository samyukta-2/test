accounts = {}

def create_account():
    acc_no = input("Enter new account number: ")
    name = input("Enter account holder name: ")
    accounts[acc_no] = {"name": name, "balance": 0}
    print("Account created successfully.")
def view_account():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        acc = accounts[acc_no]
        print("Name:", acc["name"])
        print("Balance:", acc["balance"])
    else:
        print("Account not found.")
def deposit():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_no]["balance"] += amount
        print("Deposit successful.")
    else:
        print("Account not found.")
def withdraw():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        amount = float(input("Enter amount to withdraw: "))
        if accounts[acc_no]["balance"] >= amount:
            accounts[acc_no]["balance"] -= amount
            print("Withdrawal successful.")
        else:
            print("Not enough balance.")
    else:
        print("Account not found.")

        while True:
    print("\n--- Simple Bank Menu ---")
    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        view_account()
    elif choice == "3":
        deposit()
    elif choice == "4":
        withdraw()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
