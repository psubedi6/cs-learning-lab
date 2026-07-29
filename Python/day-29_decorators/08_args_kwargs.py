def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")

        func(*args, **kwargs)

        print("After function")
    return wrapper

@simple_decorator
def greet(name):
    print(f"Hello{name}")
greet("Prakash")