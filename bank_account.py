class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount

<<<<<<< HEAD
    def withdtaw(self, amount):
=======
    def withdraw(self, amount):
>>>>>>> 5de748f2aed00c4b73a18373610cc5e3a5b513d3
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount 
            return True
        return False

    def display_balance(self):
<<<<<<< HEAD
        print(f"Current Balance: ")
        
=======
        print(f"Current Balance: ${self.account_balance:.2f} ")
>>>>>>> 5de748f2aed00c4b73a18373610cc5e3a5b513d3
