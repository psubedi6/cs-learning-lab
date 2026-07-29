class Employee:
    company = "Google"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Company: {Employee.company}")

emp1 = Employee("John", 80000)
emp2 = Employee("Bob", 5000)

emp1.display()
emp2.display()
Employee.company = "Microsoft"
emp1.display()
emp2.display()