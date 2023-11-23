import math
from typing import List
class Point:
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)
    
    @property
    def point(self):
        return self.x,self.y

class Line:
    def __init__(self,from_point, to_point):

        self.from_point = from_point
        self.to_point = to_point
     
       
    @property
    def length(self):
        a = (self.to_point.x - self.from_point.x)**2
        b = (self.to_point.y - self.from_point.y)**2
        c = (a+b)**0.5
        return c
        

class Polyline:
    def __init__(self):
        self.__segments: List[Line] = []

    @property
    def segments(self) -> List[Line]:
        return self.__segments

    @property
    def length(self) -> float:
        total_length = 0
        for segment in self.__segments:
            total_length += segment.length
        return total_length

    def add_segment(self, seg: Line) -> None:
        self.__segments.append(seg)
        
        
        
   
        
    
    