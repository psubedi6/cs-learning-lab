class Product:
    company = "Amazon"
    def __init__(self,name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

product= Product("Macbook", 1299, 25)
print(product.name)
print(product.price)
print(product.stock)
print(product.company)

phone = Product("iPhone", 1100, 24)
print(f"\n{phone.name}")
print(phone.price)
print(phone.stock)
print(phone.company)