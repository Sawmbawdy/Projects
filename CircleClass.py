class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        area = 3.14 * int(self.radius) * int(self.radius)
        return area
    def Peri(self):
        peri = 3.14 * int(self.radius) * 2
        return peri
    
circle1 = Circle(12)
print(circle1.Area())
print(circle1.Peri())