class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")

    def display_balance(self):
        print(f"Account {self.account_number} - {self.holder_name}")
        print(f"Current Balance: ₹{self.balance}")


accounts = []

def create_account():
    acc_no = input("Enter account number: ")
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial deposit amount: ₹"))
    account = BankAccount(acc_no, name, balance)
    accounts.append(account)
    print("Account created successfully!")

def find_account(acc_no):
    for acc in accounts:
        if acc.account_number == acc_no:
            return acc
    return None

def deposit_money():
    acc_no = input("Enter account number: ")
    account = find_account(acc_no)
    if account:
        amount = float(input("Enter amount to deposit: ₹"))
        account.deposit(amount)
    else:
        print("Account not found.")

def withdraw_money():
    acc_no = input("Enter account number: ")
    account = find_account(acc_no)
    if account:
        amount = float(input("Enter amount to withdraw: ₹"))
        account.withdraw(amount)
    else:
        print("Account not found.")

def check_balance():
    acc_no = input("Enter account number: ")
    account = find_account(acc_no)
    if account:
        account.display_balance()
    else:
        print("Account not found.")

while True:
    print("\n--- Bank Account Simulator ---")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit_money()
    elif choice == "3":
        withdraw_money()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        print("Thank you for using Bank Account Simulator. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
