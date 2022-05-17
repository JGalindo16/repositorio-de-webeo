from math import pi

def circle_area(radius):
    if not isinstance(radius, int):
        raise TypeError("El radio debe ser un numero")
    elif radius <0:
        raise ValueError("El radio debe ser mayor que 0")
    
    else:
        return pi * radius**2

try:
    print(circle_area(5))
    print(circle_area("tttt"))
    print(circle_area(0))
except ValueError as ex:
    print("Hubo un error")
    print(ex)
except TypeError as te:
    print("Hubo un error de tipo")
    print(te)