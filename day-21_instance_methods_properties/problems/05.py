class Square:
    def __init__(self, side):
        self.side= side
    
    @property
    def area(self):
        return self.side * self.side
    
    @area.setter
    def area(self, value):
        self.side = value ** 0.5


square = Square(4)

print(square.side)
print(square.area)
square.area = 100
print(square.side)
print(square.area)