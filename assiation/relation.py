
class BankAccount:
    def __init__(self, int_rate = 0.02, balance=0):
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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0 )
    def display_user_balance(self):
        name= self.name
        balance=self.account.balance
        print(f'user : {name}, balance: ${balance}')
        return self

awad = User("jojo", "jjj@jj.com")
awad.account.deposit(1200).yield_intrest().dispaly_account_info()