class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount

    def withdtaw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount 
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ")
        
