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
        self.x = x
        self.m = m

    def has_same_field(self, other):
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
        if isinstance(other, ModularInt) and self.has_same_field(other):
            return (self.x + other.x) % self.m
        elif isinstance(other, int):
            return (self.x + other) % self.m
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
        if isinstance(other, ModularInt) and self.has_same_field(other):
            return (self.x - other.x) % self.m
        elif isinstance(other, int):
            return (self.x - other) % self.m
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, ModularInt) and self.has_same_field(other):
            return (other.x - self.x) % self.m
        elif isinstance(other, int):
            return (other - self.x) % self.m
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, ModularInt) and self.has_same_field(other):
            return (self.x * other.x) % self.m
        elif isinstance(other, int):
            return (self.x * other) % self.m
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

        if isinstance(other, ModularInt) and self.has_same_field(other):
            other_inv = other.find_inverse()
            return (self.x * other_inv.x) % self.m
        elif isinstance(other, int):
            other_inv = ModularInt(other, self.m).find_inverse()
            return (self.x * other_inv.x) % self.m
        else:
            return NotImplemented

    def __rdiv__(self, other):
        """ other / x = other * x^(-1). """

        if isinstance(other, ModularInt) and self.has_same_field(other):
            x_inv = self.find_inverse()
            return (other.x * x_inv.x) % self.m
        elif isinstance(other, int):
            x_inv = self.find_inverse()
            return (other * x_inv.x) % self.m
        else:
            return NotImplemented

    def __truediv__(self, other):
        return self.__div__(other)

    def __rtruediv__(self, other):
        return self.__rdiv__(other)

    def __pow__(self, other):
        if isinstance(other, int):
            return pow(self.x, other, self.m)
        else:
            return NotImplemented

    def __str__(self):
        return str(self.x)
