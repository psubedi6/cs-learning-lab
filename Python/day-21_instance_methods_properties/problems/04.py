class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2
    
    @property
    def circumference(self):
        return 2 * 3.14159 * self.radius
    
circle = Circle(5)
print(circle.radius)
print(circle.circumference)
print(circle.diameter)