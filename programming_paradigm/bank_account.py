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

