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
    
awad = BankAccount(0.01)
fadi = BankAccount(10,50) 

awad.deposit(200).deposit(200).deposit(200).withdraw(500).yield_intrest().dispaly_account_info()
awad.deposit(400).deposit(200).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_intrest().dispaly_account_info()

