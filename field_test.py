# -*- coding: utf-8 -*-

"""
A set of unit tests for the encryption module's various encrpytion and decryption functions.
@author: Darren Vong
"""
import unittest

from field import IntegerField

class testField(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(testField, cls).setUpClass()
        cls.five_mod_seven = IntegerField(5, 7)

    def test_ladd(self):
        self.assertEqual(self.five_mod_seven+3, 1)

    def test_radd(self):
        self.assertEqual(3+self.five_mod_seven, 1)

    def test_lsub(self):
        self.assertEqual(self.five_mod_seven-2, 3)

    def test_rsub(self):
        self.assertEqual(7 - self.five_mod_seven, 2)

    def test_div(self):
        self.assertEqual(self.five_mod_seven/2, (5*4)%7)

    def test_pow(self):
        self.assertEqual(self.five_mod_seven**3, 6)

if __name__ == '__main__':
    unittest.main()
