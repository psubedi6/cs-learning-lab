class Course:
    semester = "Fall 2026"
    def __init__(self, course_name, instructor, credits):
        self.course_name = course_name
        self.instructor = instructor
        self.credits = credits

course1 = Course("Python", "Dr. Smith", 3)
course2 = Course("AI", "Dr. Brown", 3)

Course.semester = "Winter 2027"
course2.semester = "Spring 2027"

print(f"{course1.course_name}\n{course1.instructor}\n{course1.credits}\n{course1.semester}")
print(f"\n{course2.course_name}\n{course2.instructor}\n{course2.credits}\n{course2.semester}")