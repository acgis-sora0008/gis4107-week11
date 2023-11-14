import pytest
import math
import shapes_using_init as sh

def test_area_circle():
    expected = 12.566
    circle = sh.Circle(2)
    actual = circle.area
    assert expected == pytest.approx(actual, 0.001)
    expected = 'Circle area with a radius of 2 is 12.566'
    actual = sh.Message.output(circle)
    assert expected == actual

def test_area_square():
    expected = 9
    square = sh.Square(3)
    actual = square.area
    assert expected == pytest.approx(actual, 0.001)
    expected = 'Square area with a side of 2 is 4'
    actual = sh.Message.output(square)
    assert expected == actual

def test_area_rectangle():
    expected = 8
    rectangle = sh.Rectangle(4,2)
    actual = rectangle.area
    assert expected == pytest.approx(actual, 0.001)
    expected = 'Rectangle area with a width of 2 and height of 4 is 8'
    actual = sh.Message.output(rectangle)
    assert expected == actual