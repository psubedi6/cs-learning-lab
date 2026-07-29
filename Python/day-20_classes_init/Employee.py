class Employee:
    company = "Google"
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department= department

employee = Employee("Alice", 95000, "Engineering")
print(employee.name)
print(employee.salary)
print(employee.department)
print(employee.company)

employee1= Employee("Bob", 2600, "Maintenance")
print(employee1.name)
print(employee1.salary)
print(employee1.department)
print(employee1.company)