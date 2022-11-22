import math


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)  # zwraca string "(x, y)" obiekt klasy punkt

    def __repr__(self):  # zwraca string "Point(x, y)"
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other):  # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):  # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return (self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return (self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):  # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):  # długość wektora
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __hash__(self):
        return hash((self.x, self.y))  # bazujemy na tuple, immutable points


# Kod testujący moduł.

import unittest


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(1, 2)
        self.p2 = Point(2, 1)
        self.p3 = Point(3, 4)
        self.p4 = Point(1, 7)
        self.p5 = Point(1, 7)

    def test__str__(self):
        self.assertEqual(self.p1 == Point(1, 2), True)
        self.assertEqual(self.p1 == Point(5, 5), False)

    def test__eq__(self):
        self.assertEqual(self.p4 == self.p5, True)
        self.assertEqual(self.p3 == self.p5, False)

    def test__neg__(self):
        self.assertEqual(self.p4 != self.p5, False)
        self.assertEqual(self.p3 != self.p5, True)

    def test__add__(self):
        self.assertEqual(self.p1 + self.p2, (3, 3))
        self.assertEqual(self.p3 + self.p4, (4, 11))

    def test__sub__(self):
        self.assertEqual(self.p1 - self.p2,(-1, 1))
        self.assertEqual(self.p4 - self.p3, (-2, 3))

    def test__mul__(self):
        self.assertEqual(self.p1 * self.p2, 4)
        self.assertEqual(self.p1 * self.p3, 11)

    def test_length(self):
        self.assertEqual(self.p3.length(), 5)

    def test_cross(self):
        self.assertEqual(self.p1.cross(self.p2), -3)
        self.assertEqual(self.p2.cross(self.p3), 5)


if __name__ == '__main__':
    unittest.main()