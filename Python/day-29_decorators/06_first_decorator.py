def simpler_decorator(func):
    print("Before function")

    func()

    print("After function")

    return simpler_decorator

@simpler_decorator
def greet():
    print("Hello")

greet()