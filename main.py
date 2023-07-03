class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} units.")
        self.print_balance()

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} units.")
        else:
            print("Insufficient funds.")
        self.print_balance()

    def print_balance(self):
        print(f"Account Balance: {self.balance} units.")

    def transfer(self, amount, recipient):
        if amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            print(f"Transferred {amount} units to account number {recipient.account_number}.")
        else:
            print("Insufficient funds.")
        self.print_balance()


def main():
    accounts = {}

    while True:
        print("\n===== BANKING SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            account_number = input("Enter account number: ")
            if account_number in accounts:
                print("Account already exists.")
            else:
                accounts[account_number] = BankAccount(account_number)
                print("Account created successfully.")

        elif choice == "2":
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter the amount to deposit: "))
                accounts[account_number].deposit(amount)
            else:
                print("Account not found.")

        elif choice == "3":
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter the amount to withdraw: "))
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found.")

        elif choice == "4":
            account_number = input("Enter account number: ")
            if account_number in accounts:
                accounts[account_number].print_balance()
            else:
                print("Account not found.")

        elif choice == "5":
            account_number = input("Enter account number: ")
            recipient_number = input("Enter recipient account number: ")
            if account_number in accounts and recipient_number in accounts:
                amount = float(input("Enter the amount to transfer: "))
                accounts[account_number].transfer(amount, accounts[recipient_number])
            else:
                print("Account not found.")

        elif choice == "6":
            print("Thank you for using our banking system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
