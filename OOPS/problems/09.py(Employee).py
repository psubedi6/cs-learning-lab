class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print(f"role: {self.role}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

class Engineer(Employee):
    def __init__(self, name, age):  
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "7000")
    def showDetails(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        super().showDetails()

e1 = Engineer("Bob", 43)
e1.showDetails()