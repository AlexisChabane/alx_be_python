class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance(0)
        
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else: 
            return False
        
    def display_balance(self):
        print (f"Your current balance is: {self.account_balance} ")