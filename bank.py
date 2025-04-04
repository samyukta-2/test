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
