# -*- coding: utf-8 -*-

"""
A set of unit tests for the encryption module's various encrpytion and decryption functions.
@author: Darren Vong
"""
import unittest

from mod_int import ModularInt

class testModInt(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(testModInt, cls).setUpClass()
        cls.five_mod_seven = ModularInt(5, 7)

    def test_ladd(self):
        self.assertEqual(self.five_mod_seven+3, 1)

    def test_ladd_same_type(self):
        self.assertEqual(self.five_mod_seven+ModularInt(8,7), 13%7)

    def test_radd(self):
        self.assertEqual(3+self.five_mod_seven, 1)

    def test_radd_same_type(self):
        self.assertEqual(ModularInt(8,7)+self.five_mod_seven, 13%7)

    def test_lsub(self):
        self.assertEqual(self.five_mod_seven-2, 3)

    def test_lsub_same_type(self):
        self.assertEqual(self.five_mod_seven-ModularInt(2,7),3)

    def test_rsub(self):
        self.assertEqual(7 - self.five_mod_seven, 2)

    def test_rsub_same_type(self):
        self.assertEqual(ModularInt(7, 7)-self.five_mod_seven, 2)

    def test_mul(self):
        self.assertEqual(self.five_mod_seven * 3, 15%7)

    def test_mul_same_type(self):
        self.assertEqual(self.five_mod_seven * ModularInt(3,7), 15%7)

    def test_rmul(self):
        self.assertEqual(3 * self.five_mod_seven, 15%7)

    def test_rmul_same_type(self):
        self.assertEqual(ModularInt(3, 7) * self.five_mod_seven, 15%7)

    def test_div(self):
        self.assertEqual(self.five_mod_seven/2, (5*4)%7)

    def test_div_same_type(self):
        self.assertEqual(self.five_mod_seven/ModularInt(2,7), 6)

    def test_rdiv(self):
        self.assertEqual(2/self.five_mod_seven, 6)

    def test_rdiv_same_type(self):
        self.assertEqual(ModularInt(2,7)/self.five_mod_seven, 6)

    def test_pow(self):
        self.assertEqual(self.five_mod_seven**3, 6)

    def test_str_rep(self):
        self.assertEqual(self.five_mod_seven.__str__(), "5")

if __name__ == '__main__':
    unittest.main()
