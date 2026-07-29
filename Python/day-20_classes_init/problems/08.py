class Phone: 
    category = "Electronics"
    country = "USA"

    def __init__(self, brand, model, storage):
        self.brand = brand 
        self.model = model
        self.storage = storage

phone1 = Phone("Apple", "iPhone 17", 256)
phone2 = Phone("Samsung", "Galaxy S26", 512)

Phone.country = "Canada"

print(f"{phone1.brand}\n{phone1.model}\n{phone1.storage}\n{phone1.category}\n{phone1.country}")
print(f"{phone2.brand}\n{phone2.model}\n{phone2.storage}\n{phone2.category}\n{phone2.country}")