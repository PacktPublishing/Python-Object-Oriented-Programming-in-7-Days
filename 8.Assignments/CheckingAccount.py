# from BankAccount import BankAccount as BankAccount
# class CheckingAccount(BankAccount):
import BankAccount

class CheckingAccount(BankAccount.BankAccount):

    TRANSACTION_FEE = 50
    FREE_TRANSACTIONS = 3

    def __init__(self, initialBalance):
        # BankAccount.BankAccount.__init__(self, initialBalance)
        # super(CheckingAccount, self).__init__(initialBalance) # Python 2.7
        super().__init__(initialBalance)
        self.transactionCount = 0

    # Overriding deposit and withdraw methods
    def deposit(self, depositAmount):
        # BaseClassName.methodname(self, arguments)
        # BankAccount.BankAccount.deposit(self, depositAmount)
        # super(CheckingAccount, self).__init__(depositAmount) # Python 2.7
        super().deposit(depositAmount)
        self.transactionCount += 1

    def withdraw(self, withdrawAmount):
        # BankAccount.BankAccount.withdraw(self, withdrawAmount)
        # super(CheckingAccount, self).__init__(withdrawAmount) # Python 2.7
        super().withdraw(withdrawAmount)
        self.transactionCount += 1

    def deductFees(self):
        #print(self.transactionCount)
        if (self.transactionCount >= self.FREE_TRANSACTIONS):
            fee = self.TRANSACTION_FEE * (self.transactionCount - self.FREE_TRANSACTIONS)
            self.withdraw(fee)
        self.transactionCount = 0

    def returnTransCount(self):
        #print(self.transactionCount)
        return self.transactionCount

account3 = CheckingAccount(1200)

#account3.returnTransCount()
account3.deposit(50)
#account3.returnTransCount()
account3.withdraw(5)
account3.withdraw(5)
account3.withdraw(5)
print(account3.returnTransCount())
print(account3.getBalance())

# print(account3.getBalance())
account3.deductFees()
print(account3.getBalance())

