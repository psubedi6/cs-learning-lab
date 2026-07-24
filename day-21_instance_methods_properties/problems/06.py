class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    @property
    def balance_inr(self):
        self.balance = self.balance *65
        return self.balance *65
    
    @balance_inr.setter
    def balance_inr(self, value):
        self.balance = self.balance /65

account = BankAccount(6500)
print(account.balance)