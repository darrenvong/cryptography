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
        self.assertEqual(self.five_mod_seven+3, ModularInt(1,7))

    def test_ladd_same_type(self):
        self.assertEqual(self.five_mod_seven+ModularInt(8,7), ModularInt(6,7))

    def test_radd(self):
        self.assertEqual(3+self.five_mod_seven, ModularInt(1,7))

    def test_radd_same_type(self):
        self.assertEqual(ModularInt(8,7)+self.five_mod_seven, ModularInt(6,7))

    def test_lsub(self):
        self.assertEqual(self.five_mod_seven-2, ModularInt(3,7))

    def test_lsub_same_type(self):
        self.assertEqual(self.five_mod_seven-ModularInt(2,7),ModularInt(3,7))

    def test_rsub(self):
        self.assertEqual(7 - self.five_mod_seven, ModularInt(2,7))

    def test_rsub_same_type(self):
        self.assertEqual(ModularInt(7, 7)-self.five_mod_seven, ModularInt(2,7))

    def test_mul(self):
        self.assertEqual(self.five_mod_seven * 3, ModularInt(1,7))

    def test_mul_same_type(self):
        self.assertEqual(self.five_mod_seven * ModularInt(3,7), ModularInt(1,7))

    def test_rmul(self):
        self.assertEqual(3 * self.five_mod_seven, ModularInt(1,7))

    def test_rmul_same_type(self):
        self.assertEqual(ModularInt(3, 7) * self.five_mod_seven, ModularInt(1,7))

    def test_div(self):
        self.assertEqual(self.five_mod_seven/2, ModularInt(6,7))

    def test_div_same_type(self):
        self.assertEqual(self.five_mod_seven/ModularInt(2,7), ModularInt(6,7))

    def test_rdiv(self):
        self.assertEqual(2/self.five_mod_seven, ModularInt(6,7))

    def test_rdiv_same_type(self):
        self.assertEqual(ModularInt(2,7)/self.five_mod_seven, ModularInt(6,7))

    def test_pow(self):
        self.assertEqual(self.five_mod_seven**3, ModularInt(6,7))

    def test_str_rep(self):
        self.assertEqual(self.five_mod_seven.__str__(), "5")

    def test_equality(self):
        self.assertEqual(self.five_mod_seven, 5)

    def test_not_eq_same_class(self):
        self.assertNotEqual(self.five_mod_seven, ModularInt(6,7))

    def test_not_eq_with_int(self):
        self.assertNotEqual(self.five_mod_seven, 6)

    def test_lt_same_class(self):
        self.assertLess(self.five_mod_seven, ModularInt(6, 7))

    def test_lt_with_int(self):
        self.assertLess(self.five_mod_seven, 6)

    def test_lt_negative(self):
        self.assertFalse(self.five_mod_seven < ModularInt(4, 7))

    def test_gt_same_class(self):
        self.assertGreater(self.five_mod_seven, ModularInt(4, 7))

    def test_gt_with_int(self):
        self.assertGreater(self.five_mod_seven, 3)

    def test_gt_negative(self):
        self.assertFalse(self.five_mod_seven > 6)

    def test_ge_same_class(self):
        self.assertGreaterEqual(self.five_mod_seven, ModularInt(5, 7))
        self.assertGreaterEqual(self.five_mod_seven, ModularInt(4, 7))

    def test_ge_with_int(self):
        self.assertGreaterEqual(self.five_mod_seven, 5)
        self.assertGreaterEqual(self.five_mod_seven, 4)

    def test_ge_negative(self):
        self.assertFalse(self.five_mod_seven >= 6)

    def test_le_same_class(self):
        self.assertLessEqual(self.five_mod_seven, ModularInt(5, 7))
        self.assertLessEqual(self.five_mod_seven, ModularInt(6, 7))

    def test_le_with_int(self):
        self.assertLessEqual(self.five_mod_seven, 5)
        self.assertLessEqual(self.five_mod_seven, 6)

    def test_le_negative(self):
        self.assertFalse(self.five_mod_seven <= 3)

if __name__ == '__main__':
    unittest.main()
