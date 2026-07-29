class Laptop:
    
    category = "Electronics"
    warranty_years = 2
    def __init__(self, brand, model, price, ram):
        self.brand = brand
        self.model = model
        self.price = price
        self.ram = ram
Laptop.warranty_years = 3
laptop1 = Laptop("Apple", "MacBook Air M2", 1499, 16)
laptop2 = Laptop("Dell", "XPS 13", 1299, 32)

print(f"{laptop1.brand}\n{laptop1.model}\n{laptop1.price}\n{laptop1.ram}\n{laptop1.category}\n{laptop1.warranty_years}")

print(f"\n{laptop2.brand}\n{laptop2.model}\n{laptop2.price}\n{laptop2.ram}\n{laptop2.category}\n{laptop2.warranty_years}")