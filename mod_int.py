# -*- coding: utf-8 -*-

"""This module contains a (partial) implementation of a number mod
another integer n (i.e. Z/nZ), written to practise writing magic functions to
overload common Python operators.
@author: Darren Vong
"""
import itertools

class ModularInt(object):

    """This class represents integers modular a number m"""
    def __init__(self, x, m):
        super(ModularInt, self).__init__()
        self.m = m
        self.x = x if x < m else x % m

    def has_same_field(self, other):
        """Checks whether the 'other' number has the same field. As only my
        custom ModularInt instances are defined that way, implicitly checks
        if 'other' is an instance of a ModularInt object."""

        if isinstance(other, ModularInt):
            if self.m == other.m:
                return True
            else:
                raise TypeError("The other number has a different field to the "+
                "current number.")

    def find_inverse(self):
        """Find the inverse of x in mod 'm' - e.g. 3^-1 in F_31 is -10 or 21"""

        for i in itertools.count(start=1):
            if (i * self.x) % self.m == 0:
                return -1
            elif (i * self.x) % self.m == 1:
                return ModularInt(i, self.m)

    def __add__(self, other):
        if self.has_same_field(other):
            return ModularInt((self.x + other.x) % self.m, self.m)
        elif isinstance(other, int):
            return ModularInt((self.x + other) % self.m, self.m)
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, ModularInt):
            return self.__add__(other.x)
        elif isinstance(other, int):
            return self.__add__(other)
        else:
            return NotImplemented

    def __sub__(self, other):
        if self.has_same_field(other):
            return ModularInt((self.x - other.x) % self.m, self.m)
        elif isinstance(other, int):
            return ModularInt((self.x - other) % self.m, self.m)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if self.has_same_field(other):
            return ModularInt((other.x - self.x) % self.m, self.m)
        elif isinstance(other, int):
            return ModularInt((other - self.x) % self.m, self.m)
        else:
            return NotImplemented

    def __mul__(self, other):
        if self.has_same_field(other):
            return ModularInt((self.x * other.x) % self.m, self.m)
        elif isinstance(other, int):
            return ModularInt((self.x * other) % self.m, self.m)
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, ModularInt):
            return self.__mul__(other.x)
        elif isinstance(other, int):
            return self.__mul__(other)
        else:
            return NotImplemented

    def __div__(self, other):
        """ x / other = x * other^(-1)
        E.g in F_7, 5 / 2 = 5 * (2^(-1)) = 5 * 4 = 20 = 6
        """

        if self.has_same_field(other):
            other_inv = other.find_inverse()
            return ModularInt((self.x * other_inv.x) % self.m, self.m)
        elif isinstance(other, int):
            other_inv = ModularInt(other, self.m).find_inverse()
            return ModularInt((self.x * other_inv.x) % self.m, self.m)
        else:
            return NotImplemented

    def __rdiv__(self, other):
        """ other / x = other * x^(-1). """

        if self.has_same_field(other):
            x_inv = self.find_inverse()
            return ModularInt((other.x * x_inv.x) % self.m, self.m)
        elif isinstance(other, int):
            x_inv = self.find_inverse()
            return ModularInt((other * x_inv.x) % self.m, self.m)
        else:
            return NotImplemented

    def __truediv__(self, other):
        return self.__div__(other)

    def __rtruediv__(self, other):
        return self.__rdiv__(other)

    def __pow__(self, other):
        if isinstance(other, int):
            return ModularInt(pow(self.x, other, self.m), self.m)
        else:
            return NotImplemented

    def __str__(self):
        return str(self.x)

    def __repr__(self):
        return "ModularInt(%d, %d)" % (self.x, self.m)

    def __eq__(self, other):
        if self.has_same_field(other) and self.x == other.x:
            return True
        elif isinstance(other, int) and other == self.x:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if self.has_same_field(other) and self.x < other.x:
            return True
        elif isinstance(other, int) and self.x < other:
            return True
        else:
            return False

    def __le__(self, other):
        if self.__lt__(other) or self.__eq__(other):
            return True
        else:
            return False

    def __gt__(self, other):
        if self.__lt__(other) or self.__eq__(other):
            return False
        else:
            return True

    def __ge__(self, other):
        if self.__gt__(other) or self.__eq__(other):
            return True
        else:
            return False
