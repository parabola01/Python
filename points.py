import math


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)  # zwraca string "(x, y)" obiekt klasy punkt

    def __repr__(self):  # zwraca string "Point(x, y)"
        return "Point({} ,{})".format(self.x, self.y)

    def __eq__(self, other):  # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):  # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        x = self.x + other.x
        y = self.y + other.y

        return (x, y)

    def __sub__(self, other):  # v1 - v2
        x = self.x - other.x
        y = self.y - other.y

        return (x, y)

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
    def test__str__(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        p3 = Point(3, 4)
        p4 = Point(5, 5)
        self.assertEqual(p1 == Point(1, 2), True)
        self.assertEqual(p1 == Point(3, 3), False)

    def test_length(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        p3 = Point(3, 4)
        p4 = Point(5, 5)
        self.assertEqual(p2.length(), 5)

    def test_cross(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        p3 = Point(3, 4)
        p4 = Point(5, 5)
        self.assertEqual(p1.cross(p2), -2)
        self.assertEqual(p2.cross(p3), 0)

    def test__mul__(self):
        p1 = Point(1, 2)
        p2 = Point(2, 4)
        p4 = Point(5, 5)
        self.assertEqual(p1 * p2, 10)
        self.assertEqual(p1 * p4, 15)

    def test__sub__(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        p3 = Point(3, 4)
        self.assertEqual(p1 - p2,(-2, -2))
        self.assertEqual(p3 - p2, (0, 0))

    def test__add__(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        p3 = Point(3, 4)
        self.assertEqual(p1 + p2, (4, 6))
        self.assertEqual(p3 + p2, (6, 8))


if __name__ == '__main__':
    unittest.main()
