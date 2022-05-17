"""
(Fundamental hacer un dibujo para lograr entender lo que vamos a hacer)
Vamos a hacer ejercicios de la clase pasada :

"""

from circle import Circle
from rectangle import Rectangle
from triangle import Triangle

my_triangle=Triangle(5, 5)
my_rectangle = Rectangle(5, 3)
circle = Circle(3)
circle.greet()
my_rectangle.greet()
print(my_triangle.area())