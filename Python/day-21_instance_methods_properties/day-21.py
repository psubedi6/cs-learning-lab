"""class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance= balance

    def deposit(self, account):
        self.balance += account

    def withdraw(self, account):
        self.balance -= account

acc1 = BankAccount("Prakash", 500)
acc2 = BankAccount("Bob", 1000)

acc1.deposit(100)
acc2.withdraw(100)

print(acc1.balance)
print(acc2.balance)"""


class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    
    @property
    def age(self):
        return 2026 - self.birth_year
    
    @age.setter
    def age(self, value):
        self.birth_year = 2026 - value

person = Person("Prakash", 2003)
print(person.age)