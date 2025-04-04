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
