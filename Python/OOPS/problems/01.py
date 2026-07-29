class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("HELLO WORLD")

    def average(self):
        sum = 0
        for value in self.marks:
            sum = sum + value
        print(f"hi, {self.name} your average score is: {sum}")

s1 = Student("Bob", [74,86,23])
s1.average()

s1.name 