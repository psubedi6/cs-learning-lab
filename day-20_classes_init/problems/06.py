class Employee:
    company = "Google"
    def __init__(self, name, salary):
        self.name = name
        self.salary= salary

employee1 = Employee("Alice", 90000)
employee2 = Employee("Bob", 80000)
employee1.company = "Microsoft"
print(f"{employee1.name}\n{employee1.salary}\n{employee1.company}")
print(f"\n{employee2.name}\n{employee2.salary}\n{employee2.company}")