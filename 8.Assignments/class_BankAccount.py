'''
Create a class BankAccount having "balance" set to initial balance
which is already existing in the account.
Create a method called "deposit" to account for any deposits to the account.
And create a method "withdraw" to account for any withdrawal from the account.
'''
class BankAccount:

    def __init__(self, initialBalance):
        self.balance = initialBalance

    def deposit(self, depositAmount):
        self.balance += depositAmount
        print(self.balance)

    def withdraw(self, withdrawAmount):
        if (withdrawAmount > self.balance):
            print("Insufficient Funds!!!")
            return False
        else:
            self.balance -= withdrawAmount
            print("Withdrawn Amout", self.balance)
            return True


account = BankAccount(1000)
account.deposit(500)
account.withdraw(50)