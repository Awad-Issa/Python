class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount	
    def make_withdraw(self, amount):	
        self.account_balance -= amount
    def display_user_balance(self):
        name= self.name
        balance=self.account_balance
        print(f'user : {name}, balance: ${balance}')

class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self,amount):
        self.balance -= amount
        return self
    def dispaly_account_info(self):
        print(f'Balance: ${self.balance}')
        return self
    def yield_intrest(self):
        self.balance += self.balance * self.int_rate
        return self