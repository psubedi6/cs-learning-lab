class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def Area(self):
        area = (22/7) * self.radius *self.radius
        print(f"The area is: {area}")
        
    def Perimeter(self):
        perimeter = 2 * (22/7) * self.radius
        print(f"The perimeter is: {perimeter}")
    
value = Circle(21)
value.Area()
value.Perimeter()