class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance

#Depositing method
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount

#Withdrawal method
    def withdraw(self, amount):
        if amount > 0 and self.__account_balance >= amount:
            self.__account_balance -= amount
            return True #Withdrawal successful
        elif amount > self.__account_balance:
            return False #Withdrawal failed

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")

# main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()

