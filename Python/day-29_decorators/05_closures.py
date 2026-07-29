def outer(name):

    def inner():
        print(f"Hello {name}")

    return inner


greet_prakash = outer("Prakash")

greet_john = outer("John")


greet_prakash()

greet_john()