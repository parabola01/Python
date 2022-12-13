import pytest
from rectangle import Rectangle
from points import Point

def test_from_points():
    r1 = Rectangle.from_points((Point(1,2), Point(3,4)))
    r2 = Rectangle(1,2,3,4)

    assert r1 == r2

def test_property1():
    r = Rectangle(1, 2, 3, 4)

    assert r.top == 4
    assert r.left == 1
    assert r.bottom == 2
    assert r.right == 3
    assert r.width == 2
    assert r.height == 2

def test_property2():
    point1 = Point(1,2)
    point2 = Point(3,4)

    r = Rectangle.from_points((point1, point2))

    assert r.topright == point2
    assert r.topleft == Point(point1.x, point2.y)
    assert r.bottomright == Point(point2.x, point1.y)
    assert r.bottomleft == point1
