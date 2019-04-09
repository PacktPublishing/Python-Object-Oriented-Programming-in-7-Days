'''
Create a subclass SavingsAccount of BankAccount
All methods of BankAccount work with SavingsAccount
add instance variable interestRate (balance is inherited)
add method addPeriodicInterest
'''

import BankAccount

class SavingsAccount(BankAccount.BankAccount):

    def __init__(self, initialBalance, interestRate):
        # The __init__ method of SavingsAccount class explicitly
        # invokes the __init__method of the BankAccount class.
        super().__init__(initialBalance)
        # super(SavingsAccount, self).__init__(initialBalance)
        # BankAccount.BankAccount.__init__(self, initialBalance)
        self.interestRate = interestRate
        print(initialBalance)

    def addPeriodicInterest(self):
        interest = self.getBalance() * self.interestRate / 100.0;
        self.deposit(interest)

account3 = SavingsAccount(1200, 5)
account3.deposit(50)
