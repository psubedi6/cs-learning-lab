"""Question 1 — Student Class (Basics of OOP)

Create a class called Student.

Requirements
The constructor should accept:
name
marks
Store both as instance attributes.
Create an instance method named display() that prints:
Student: Alice
Marks: 92
Create two different Student objects and call display() for both."""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Student: {self.name}")
        print(f"Marks: {self.marks}")

student1 = Student("Alice", 92)
student2 = Student("Bob", 69)

student1.display()
student2.display()