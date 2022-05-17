from figure import Figure
from math import pi

class Circle(Figure):
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        return pi * self.radius**2
    
    def perimeter(self):
        return self.radius * pi * 2

    def get_type(self):
        return "circulo"
    