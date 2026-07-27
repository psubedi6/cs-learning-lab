class Animal:
    def make_sound(self):
        print("Some generic animal sound")


class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Woof! Woof!")

class GuideDog(Dog):
    def __init__(self):
        super().__init__()

dog = Dog()
dog.make_sound()
