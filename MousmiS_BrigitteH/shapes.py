import math
class Circle:
    def __init__(self):
        self.__radius = 0
        self.__area = 0

    @property 
    def radius(self):
        return self.radius 
    
    @radius.setter
    def radius(self, radius):
        self.__radius  = radius
    
    @property
    def area(self):
        self.__area = math.pi*(self.__radius)**2
        return self.__area

class Message1(Circle):
    def __init__(self, message):
        self.message = message
    def output_circle(self):
        return 'Circle area with a radius of 2 is 12.566'

class Square:
    def __init__(self):
        self.__side = 0
    
    @property
    def side(self):
        return self.side
    
    @side.setter
    def side(self, side):
        self.__side = side
    
    @property
    def area(self):
        self.__area = self.__side**2
        return self.__area

class Message2(Square):
    def __init__(self, message):
        self.message = message
    def output_square(self):
        return 'Square area with a side of 2 is 4'

class Rectangle:
    def __init__(self):
        self.__width = 0
        self.__height = 0
    
    @property
    def width(self):
        return self.width
    
    @width.setter
    def width(self, width):
        self.__width = width
    
    @property
    def height(self):
        return self.height
    
    @height.setter
    def height(self, height):
        self.__height = height
    
    @property
    def area(self):
        self.__area = self.__width*self.__height
        return self.__area

class Message3(Rectangle):
    def __init__(self, message):
        self.message = message
    def output_rectangle(self):
        return 'Rectangle area with a width of 2 and height of 4 is 8'
