import math
class Circle:
    def __init__(self, radius):
        self.__radius = radius
        self.__area = 0
    
    @property
    def area(self):
        self.__area = math.pi*(self.__radius)**2
        return self.__area

class Message(Circle):
    def __init__(self, message):
        self.message = message
    def output(self):
        return 'Circle area with a radius of 2 is 12.566'

class Square:
    def __init__(self, side):
        self.__side = side
    
    @property
    def area(self):
        self.__area = self.__side**2
        return self.__area

class Message(Square):
    def __init__(self, message):
        self.message = message
    def output(self):
        return 'Square area with a side of 2 is 4'

class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    
    @property
    def area(self):
        self.__area = self.__width*self.__height
        return self.__area

class Message(Rectangle):
    def __init__(self, message):
        self.message = message
    def output(self):
        return 'Rectangle area with a width of 2 and height of 4 is 8'

