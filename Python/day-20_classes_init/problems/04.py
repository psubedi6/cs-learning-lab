class BankAccount:
    bank_name = "Royal Bank"
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

account1 = BankAccount("Prakash", "RB1001", 1500)
account2 = BankAccount("Alice", "RB1002", 3000)

print(f"{account1.account_holder}\n{account1.account_number}\n{account1.balance}\n{account1.bank_name}")
print(f"{account2.account_holder}\n{account2.account_number}\n{account2.balance}\n{account2.bank_name}")

account1.balance = 2000

print(f"\n{account1.account_holder}\n{account1.account_number}\n{account1.balance}\n{account1.bank_name}")
print(f"{account2.account_holder}\n{account2.account_number}\n{account2.balance}\n{account2.bank_name}")