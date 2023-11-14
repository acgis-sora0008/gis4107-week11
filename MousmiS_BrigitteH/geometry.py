class Point:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    
    @property
    def point(self):
        return self.__x,self.__y

class Line:
    def __init__(self,from_point, to_point):
        self.__from_point = from_point
        self.__to_point = to_point
    
    @property
    def length(self):
        from_point = Point()
        to_point = Point()
        self.__length = ((to_point.__x - from_point.__x)**2 + (to_point.__y - from_point.__y)**2)**0.5
        return self.__length