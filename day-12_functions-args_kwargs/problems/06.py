def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print()
student_info(name = "Prakash", age =24)