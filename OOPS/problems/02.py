#What i wrote
class Account:
    balance = 0
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
    
    def debit(self, amount):
        self.balance += amount
        print(self.get_balance())
    

    def credit(self, amount):
        self.balance -= amount
        print(self.get_balance())

    def get_balance(self):
        return self.balance
    
account1 = Account(5004, 205519)
account1.debit(100)
account1.credit(900) 