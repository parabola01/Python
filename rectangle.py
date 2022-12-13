from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):

        if x1 >= x2 or y1 >= y2:
            raise ValueError("Try again, invalid value!")
        else:
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)

    def __str__(self):  # "[(x1, y1), (x2, y2)]"
        return "[({},{}), ({},{})]".format(self.pt1.__str__(), self.pt2.__str__())

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle" + self.__str__()

    def __eq__(self, other):  # obsługa rect1 == rect2
        if isinstance(other, Rectangle):
            return self.pt1 == other.pt1 and self.pt2 == other.pt2
        else:
            raise ValueError("Try again, invalid value of other!")

    def __ne__(self, other):  # obsługa rect1 != rect2
        if isinstance(other, Rectangle):
            return not self == other
        else:
            raise ValueError("Try again, invalid value of other!")

    def center(self):  # zwraca środek prostokąta
        x = (self.pt1.x + self.pt2.x) / 2
        y = (self.pt1.y + self.pt2.y) / 2

        return Point(x, y)

    def area(self):  # pole powierzchni
        a = self.pt1.x - self.pt2.x
        b = self.pt1.y - self.pt2.y
        return abs(a * b)

    def move(self, x, y):  # przesunięcie o (x, y)
        self.pt1.x = self.pt1.x + x
        self.pt1.y = self.pt1.y + y
        self.pt2.x = self.pt2.x + x
        self.pt2.y = self.pt2.y + y

    def intersection(self, other):
        if isinstance(other, Rectangle):
            new_x1 = max(self.pt1.x, other.pt1.x)
            new_x2 = min(self.pt2.x, other.pt2.x)
            new_y1 = max(self.pt1.y, other.pt1.y)
            new_y2 = min(self.pt2.y, other.pt2.y)
            return Rectangle(new_x1, new_y1, new_x2, new_y2)
        else:
            raise ValueError("Try again, invalid value of other!")

    def cover(self, other):  # prostąkąt nakrywający oba
        if isinstance(other, Rectangle):
            new_x1 = min(self.pt1.x, other.pt1.x)
            new_x2 = max(self.pt2.x, other.pt2.x)
            new_y1 = min(self.pt1.y, other.pt1.y)
            new_y2 = max(self.pt2.y, other.pt2.y)
            return Rectangle(new_x1, new_y1, new_x2, new_y2)
        else:
            raise ValueError("Try again, invalid value of other!")

    def make4(self):  # zwraca krotkę czterech mniejszych
        xM = self.pt1.x + ((self.pt2.x - self.pt1.x) / 2)
        yM = self.pt1.y + ((self.pt2.y - self.pt1.y) / 2)

        r1 = Rectangle(self.pt1.x, self.pt1.y, xM, yM)
        r2 = Rectangle(xM, self.pt1.y, self.pt2.x, yM)
        r3 = Rectangle(self.pt1.x, yM, xM, self.pt2.y)
        r4 = Rectangle(xM, yM, self.pt2.x, self.pt2.y)

        return ([r1, r2, r3, r4])

    @classmethod
    def from_points(cls, points):
        point1, point2 = points
        if not (isinstance(point1, Point) and isinstance(point2, Point)):
            raise ValueError("Argument is not iterable of points")
        return cls(point1.x, point1.y, point2.x, point2.y)

    @property
    def topleft(self):
        return Point(self.pt1.x, self.pt2.y)

    @property
    def bottomleft(self):
        return self.pt1

    @property
    def topright(self):
        return self.pt2

    @property
    def bottomright(self):
        return Point(self.pt2.x, self.pt1.y)

    @property
    def top(self):
        return self.pt2.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def right(self):
        return self.pt2.x

    @property
    def width(self):
        return self.pt2.x - self.pt1.x

    @property
    def height(self):
        return self.pt2.y - self.pt1.y



# A-------B   po podziale  A---+---B
# |       |                |   |   |
# |       |                +---+---+
# |       |                |   |   |
# D-------C                D---+---C

# Kod testujący moduł.

import unittest

p1 = Point(1, 2)
p2 = Point(3, 4)
p4 = Point(5, 5)

r1 = Rectangle(p1.x, p1.y, p2.x, p2.y)
r2 = Rectangle(p1.x, p1.y, p2.x, p2.y)
r3 = Rectangle(p2.x, p2.y, p4.x, p4.y)


class TestRectangle(unittest.TestCase):

    def test__str__(self):
        self.assertEqual(r1 == Rectangle(1, 2, 2, 6), False)
        self.assertEqual(r2 == Rectangle(1, 2, 3, 4), True)
        self.assertEqual(r3 == Rectangle(2, 2, 6, 10), False)

    def test__eq__(self):
        self.assertEqual(r1 == r2, True)
        self.assertEqual(r1 == r3, False)
        self.assertEqual(r2 == r3, False)

    def test__ne__(self):
        self.assertEqual(r1 != r3, True)
        self.assertEqual(r2 != r3, True)

    def test__center__(self):
        self.assertEqual(r2.center() == Point(2, 3), True)
        self.assertEqual(r2.center() == Point(1, 1), False)
        self.assertEqual(r3.center() == Point(2, 2), False)

    def test__area__(self):
        self.assertEqual((r1.area() == 1), False)
        self.assertEqual((r2.area() == 3), False)

    def test__move__(self):
        r1.move(1, 2)
        self.assertEqual(r1 == Rectangle(2, 4, 4, 6), True)
        self.assertEqual(r1 == Rectangle(1, 2, 3, 4), False)
        r3.move(2, 2)
        self.assertEqual(r2 == Rectangle(1, 1, 2, 3), False)

    def test__cover(self):
        self.assertEqual((r1.cover(r2) == r1), True)
        self.assertEqual((r2.cover(r1) == r2), True)
        self.assertEqual((r1.cover(r2) == r3), False)

    def test__intersection(self):
        self.assertEqual((r1.cover(r2) == r1), True)
        self.assertEqual((r3.cover(r2) == r1), False)

    def test__make4__(self):
        self.assertEqual((r1.make4() == (r1, r2, r3, r1)), False)
        self.assertEqual((r2.make4() == (r2, r2, r3, r1)), False)

