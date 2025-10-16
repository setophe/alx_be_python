class BankAccount:

    #ATTRIBUTES and CONSTRUCTOR
    def __init__(self, account_balance = 0 ):
        self.account_balance = account_balance

    #METHODS
    def deposit(self,amount):
        self.account_balance += amount

    def withdraw(self,amount):
        if self.account_balance <= amount:
            return False
        else:
            self.account_balance -= amount

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")