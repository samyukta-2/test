accounts = {}

def create_account():
    acc_no = input("Enter new account number: ")
    name = input("Enter account holder name: ")
    accounts[acc_no] = {"name": name, "balance": 0}
    print("Account created successfully.")

