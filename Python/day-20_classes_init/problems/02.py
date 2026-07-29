class Student:
    school = "Algoma University"
    def __init__(self,name, student_id, gpa):
        self.name= name
        self.student_id= student_id
        self.gpa = gpa

student1= Student("Prakash", "A001", 3.6)
student2 = Student("John", "A002", 3.9)

print(f"{student1.name}\n{student1.student_id}\n{student1.gpa}\n{student1.school}")
print(f"\n{student2.name}\n{student2.student_id}\n{student2.gpa}\n{student2.school}")
