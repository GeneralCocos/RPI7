import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1) 
import math  # Импорт модуля math для доступа к значению числа Пи

class Geometric:
    def calculateArea(self):
        print("Calculating area")

class Square(Geometric):
    def __init__(self, a):
        self.side = a
        
    def _perimeter(self):
        print("Perimeter of Square {}: {}\n".format(self.side, self.side*4))
    
    def calculateArea(self):
        print("Area of Square {}: {}\n".format(self.side, pow(self.side, 2)))

class Circle(Geometric):  # Circle, унаследован от Geometric
    def __init__(self, radius):
        self.__radius = radius  # приватнйй атрибута radius
    
    def calculateArea(self):  # Переопределение метода calculateArea() для расчета площади окружности
        area = math.pi * (self.__radius ** 2)  #  Pi * r^2
        print("Площадь окружности {}: {:.2f}\n".format(self.__radius, area))

geom = Geometric()
geom.calculateArea()
sq = Square(5)
sq.calculateArea()
sq._perimeter()

cir = Circle(3)  # объект класса Circle с радиусом 3
cir.calculateArea()  # Вызов метода calculateArea() для объекта класса Circle

print("Check subclass Square: ", issubclass(Square, Geometric))
print("Check subclass Circle: ", issubclass(Circle, Geometric))

print("Check instance sq -> Square: ", isinstance(sq, Square))
print("Check instance sq -> Geometric: ", isinstance(sq, Geometric))
print("Check instance sq -> dict: ", isinstance(sq, dict))

print("Geometric.__bases__: ", Geometric.__bases__)
print("Square.__bases__: ", Square.__bases__)
print("Circle.__bases__: ", Circle.__bases__)
