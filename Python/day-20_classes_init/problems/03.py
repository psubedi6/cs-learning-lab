class Car:
    wheels = 4
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Tesla", "Model 3", 2025)

car1.model = "Camry"
print(f"{car1.brand}\n{car1.model}\n{car1.year}\n{car1.wheels}")
print(f"\n{car2.brand}\n{car2.model}\n{car2.year}\n{car2.wheels}")