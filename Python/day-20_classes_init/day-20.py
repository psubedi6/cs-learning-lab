class Product:
         company = "Amazon"
         def __init__(self, name):
                self.name = name

laptop = Product("MacBook Air M2")
phone = Product("iPhone 17")
keyboard = Product("Mechanical Keyboard")

print(laptop.name)
print(phone.name)
print(keyboard.name)

phone.name = "Samsung Galaxy S26"
print(laptop.name)
print(phone.name)
print(keyboard.name)

print(laptop.company)
print(phone.company)
print(keyboard.company)