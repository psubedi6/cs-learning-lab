def say_hello():
    print("Hello!")
say_hello()


def say_hello(name):
    print("Hello", name)
say_hello("Prakash")
say_hello("Alice")
say_hello("Bob")


def introduce(name, age):
    print("Name:", name)
    print("Age:", age)
introduce("Prakash", 24)


def introduce(name, age):
    print("Name:", name)
    print("Age:", age)
print("Example 1")
introduce("Prakash", 24)
print()#provides space
print("Example 2")
introduce(name="Prakash", age=24)
print()
print("Example 3")
introduce(age=24, name="Prakash")
print()
print("Example 4")
introduce("Prakash", age=24)


def introduce(name, age=18):
    print("Name:", name)
    print("Age:", age)
print("Example 1")
introduce("Prakash")
print()
print("Example 2")
introduce("Prakash", 24)
print()
print("Example 3")
introduce(name="Alice")
print()
print("Example 4")
introduce(name="Bob", age=30)



def profile(name, country="Canada", *args, **kwargs):
    print("Name:", name)
    print("Country:", country)
    print("Args:", args)
    print("Kwargs:", kwargs)
print("Example 1")
profile("Prakash")
print()
print("Example 2")
profile("Prakash", "Nepal")
print()
print("Example 3")
profile("Prakash", "Nepal", "Python", "Git")
print()
print("Example 4")
profile(
    "Prakash",
    "Nepal",
    "Python",
    "Git",
    hobby="Gaming",
    age=24,
    university="Algoma University"
)