class BankAccount:
    bank_name = "RBC"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount



    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance -  amount
        else:
            print("Insufficient balance")

    def display(self):
        print(f"Bank: {BankAccount.bank_name}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

acc=BankAccount("Alice", 1500)
acc.deposit(500)
acc.withdraw(100)
acc.withdraw(5000)

acc.display()