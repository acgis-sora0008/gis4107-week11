import pytest
import math
import shapes as sh

def test_area_circle():
    expected = 12.566
    circle = sh.Circle()
    circle.radius = 2
    actual = circle.area
    assert expected == pytest.approx(actual, 0.001)
    expected = 'Circle area with a radius of 2 is 12.566'
    actual = sh.Message1.output_circle(circle)
    assert expected == actual

def test_area_square():
    expected = 9
    square = sh.Square()
    square.side = 3
    actual = square.area
    assert expected == pytest.approx(actual, 0.001)
    expected = 'Square area with a side of 2 is 4'
    actual = sh.Message2.output_square(square)
    assert expected == actual

def test_area_rectangle():
    expected = 8
    rectangle = sh.Rectangle()
    rectangle.width = 4
    rectangle.height = 2
    actual = rectangle.area
    assert expected == pytest.approx(actual, 0.001)
    expected = 'Rectangle area with a width of 2 and height of 4 is 8'
    actual = sh.Message3.output_rectangle(rectangle)
    assert expected == actual
