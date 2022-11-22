from math import gcd

class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        assert y != 0
        self.x = int(x)
        self.y = int(y)
        fr = gcd(self.y, self.x)
        if fr > 1:
            self.x /= fr
            self.y /= fr

    def __str__(self): # zwraca "x/y" lub "x" dla y=1
        return "{}".format(self.x) if self.y == 1 else "{}/{}".format(self.x, self.y)

    def __repr__(self):        # zwraca "Frac(x, y)"
        return "Frac({}, {})".format(self.x, self.y)

    #def __cmp__(self, other): pass  # cmp(frac1, frac2)    # Py2

    def __eq__(self, other):     # Py2.7 i Py3
        if self.x == self.y and other.x == other.y:
            return True
        elif self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __ne__(self, other):  # !=
        return not self == other

    def __lt__(self, other): # <
        return True if self.x/self.y < other.x/other.y else False

    def __le__(self, other): # <=
        if (Frac.__lt__(self,other) == True) or (Frac.__eq__(self,other) == True):
            return True
        else:
            return False

    def __gt__(self, other):  # >
        return not self <= other

    def __ge__(self, other):  # >=
        return not self < other

    def __add__(self, other):  # frac1 + frac2
        return Frac(self.x * other.y + self.y * other.x, self.y * other.y)

    def __sub__(self, other):  # frac1 - frac2
        return Frac(self.x * other.y - self.y * other.x, self.y * other.y)

    def __mul__(self, other):  # frac1 * frac2
        return Frac(self.x * other.x, self.y * other.y)

    # def __div__(self, other): pass  # frac1 / frac2, Py2

    def __truediv__(self, other):  # frac1 / frac2, Py3
        return Frac(self.x * other.y, self.y * other.x)

    def __floordiv__(self, other): pass  # frac1 // frac2, opcjonalnie

    def __mod__(self, other): pass  # frac1 % frac2, opcjonalnie

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
            return Frac(self.x, self.y)

    def __neg__(self):  # -frac = (-1)*frac
        if self.x/self.y > 0:
            return Frac(-self.x, self.y)
        else:
            return Frac(self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):       # float(frac)
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # w Pythonie set([2]) == set([2.0])
        # chcemy set([2]) == set([Frac(2)])

# Kod testujący moduł.

import unittest

class TestFrac(unittest.TestCase):
    def setUp(self):
        self.f1 = Frac(1, 3)
        self.f2 = Frac(3, 9)
        self.f3 = Frac(0, 2)
        self.f4 = Frac(2, 3)
        self.f5 = Frac(5, 1)
        self.f6 = Frac(- 3, 2)
        self.f7 = Frac(1, 5)

    def test__str__(self):
        self.assertEqual(self.f5, Frac(5/1))
        self.assertEqual(self.f3, Frac(0/2))

    def test__eq__(self):
        self.assertEqual(self.f1 == self.f2, True)
        self.assertEqual(self.f2 == self.f4, False)

    def test__ne__(self):
        self.assertEqual(self.f1 != self.f2, False)
        self.assertEqual(self.f2 != self.f4, True)

    def test__lt__(self):
        self.assertEqual(self.f1 < self.f2, False)
        self.assertEqual(self.f1 < self.f4, True)

    def test__le__(self):
        self.assertEqual(self.f1 <= self.f2, True)
        self.assertEqual(self.f1 <= self.f4, True)

    def test__gt__(self):
        self.assertEqual(self.f1 > self.f2, False)
        self.assertEqual(self.f4 > self.f1, True)

    def test__ge__(self):
        self.assertEqual(self.f1 >= self.f2, True)
        self.assertEqual(self.f1 >= self.f4, False)
        self.assertEqual(self.f4 >= self.f1, True)

    def test__add__(self):
        self.assertEqual(self.f1 + self.f2, Frac(2,3))
        self.assertEqual(self.f3 + self.f4, Frac(2,3))

    def test__sub__(self):
        self.assertEqual(self.f1 - self.f2, Frac(0))
        self.assertEqual(self.f3 - self.f4, Frac(-2,3))

    def test__mul__(self):
        self.assertEqual(self.f1 * self.f2, Frac(1,9))
        self.assertEqual(self.f2 * self.f5, Frac(5,3))

    def test__truediv__(self):
        self.assertEqual(self.f1 / self.f2, Frac(1))
        self.assertEqual(self.f2 / self.f5, Frac(1, 15))

    def test__pos__(self):
        self.assertEqual(+self.f6, Frac(-3,2))
        self.assertEqual(+self.f2, Frac(1,3))

    def test__neg__(self):
        self.assertEqual(-self.f6, Frac(-3,2))
        self.assertEqual(-self.f2, Frac(-1,3))

    def test__invert__(self):
        self.assertEqual(~self.f1, Frac(3,1))
        self.assertEqual(~self.f2, Frac(3))

    def test__float__(self):
        self.assertEqual(float(self.f7), 0.2)

if __name__ == '__main__':
    unittest.main()