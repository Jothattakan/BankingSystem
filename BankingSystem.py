import random


class BankAccount:
    def __init__(self, name, account_number, pin, balance=0):
        self.name = name
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. Your new balance is {self.balance}")
        else:
            print("Invalid amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. Your new balance is {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def check_balance(self):
        print(f"Your current balance is {self.balance}")


def main():  # creating dictionary for to store account information
    accounts = {}

    def create_account():
        name = input("Enter your name: ")
        account_number = "BAC" + "".join(str(random.randint(0, 6)) for _ in range(6))
        pin = input("Enter a 4-digit PIN: ")

        if account_number in accounts:
            print("Account number already exists. Please try again")
            return

        if len(pin) == 4 and pin.isdigit():
            accounts[account_number] = BankAccount(name, account_number, pin)
            print(f"Account created successfully.\nAccount Name:{name}.\nAccount Number:{account_number}.")

        else:
            print(f"Invalid PIN, please set 4-digit numeric PIN")

    def login():
        account_number = input("Enter the account number: ")
        pin = input("Enter the PIN: ")

        if account_number in accounts and accounts[account_number].pin == pin:
            print("Login successful")
            return accounts[account_number]
        else:
            print("Invalid Account number or PIN.")
            return None

    while True:
        print("Welcome To The Banking System")
        print("1. Create Bank Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            account = login()
            if account:
                while True:
                    print("1. Deposit")
                    print("2. Withdrawal")
                    print("3. Check Balance")
                    print("4. logout")

                    option = input("Enter the option: ")
                    if option == "1":
                        try:
                            amount = float(input("Enter the amount to deposit: "))
                            account.deposit(amount)
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                    elif option == "2":
                        try:
                            amount = float(input("Enter the amount to withdraw: "))
                            account.withdraw(amount)
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                    elif option == "3":
                        account.check_balance()
                    elif option == "4":
                        print("Logged out")
                        break
                    else:
                        print("Invalid option")
        elif choice == "3":
            print("Thank you for using the Banking System.")
            break
        else:
            print("Invalid Choice, try again")


main()
