import pytest
import geometry as ge
from geometry import Point, Line, Polyline

def test_point():
    expected = 45.2059, 75.5417
    point = ge.Point(45.2059,75.5417)
    actual = point.point
    assert expected == actual

def test_line_length():
    from_point = Point(2, 3)
    to_point = Point(5, 7)
    expected = 5
    line = ge.Line(from_point, to_point)
    actual = line.length
    assert expected == actual
    
    
    
def test_polyline_add_segments():
    point1 = Point(2,3)
    point2 = Point(5,7)
    line = Line(point1, point2)
    polyline = Polyline()
    polyline.add_segment(line)
    expected = 5
    # assert len(polyline.segments) == 1
    actual = polyline.length
    assert expected == actual
    
    
     