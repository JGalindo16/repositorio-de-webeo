from figure import Figure

class Triangle(Figure):
    def __init__(self, height, base):
        self.height = height
        self.base = base
    
    def area(self):
        return (self.height * self.base)/2
    
    def perimeter(self):
        return (self.base*3)

    def get_type(self):
        return "Triangulo"