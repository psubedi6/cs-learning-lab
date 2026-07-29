class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
    
    def add_marks(self,amount):
        self.marks += amount

student = Student("Prakash", 80)
student.add_marks(15)
print(student.marks)