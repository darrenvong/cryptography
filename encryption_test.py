# -*- coding: utf-8 -*-

"""
A set of unit tests for the encryption module's various encrpytion and decryption functions.
@author: Darren Vong
"""
import unittest

import numpy as np
from numpy.testing import assert_equal

import encryption
from encryption import NUMS_TO_ALPHABET_MOD26, NUMS_TO_ALPHABET_MOD29

class testEncryption(unittest.TestCase):

    def test_affine_encrypt(self):
        K = np.array([[5,5],[5,8]])
        L = [9,2]
        m = [18,7]
        encrypted_text = encryption.affine_encrypt(K,L,m,NUMS_TO_ALPHABET_MOD29)
        expected = 'SD'
        self.assertEqual(encrypted_text, expected)

    def test_affine_encrypt_1D(self):
        k, l = 9, 19
        m = np.array([18,7,14,14,19])
        encrypted_text = encryption.affine_encrypt(k,l,m,NUMS_TO_ALPHABET_MOD26,mod=26)
        expected = 'ZEPPI'
        self.assertEqual(encrypted_text, expected)

    def test_caesar_encrypt(self):
        k = 16
        m = np.array([18,19,14,15])
        encrypted_text = encryption.caesar_encrypt(k,m)
        expected = 'IJEF'
        self.assertEqual(encrypted_text, expected)

    def test_caesar_decrypt(self):
        k = 16
        e_m = np.array([19,7,4,5])
        decrypted_text = encryption.caesar_decrypt(k, e_m)
        self.assertEqual(decrypted_text, 'DROP')

    def test_inv_2x2(self):
        M = np.array([[5,5],[5,8]])
        M_inv = encryption.inverse_2x2_matrix(M, 29)
        expected = np.array([[16,19],[19,10]])
        assert_equal(M_inv, expected)

    def test_find_inverse(self):
        inv = encryption.find_inverse(15,29)
        self.assertEqual(inv, 2)

    def test_find_inverse_negative(self):
        inv = encryption.find_inverse(2,6)
        self.assertEqual(inv, -1)

    def test_affine_decrypt(self):
        K = np.array([[5,5],[5,8]])
        L, M = [9,2], [20,12]
        decrypted_text = encryption.affine_decrypt(K, L, M, NUMS_TO_ALPHABET_MOD29)
        expected = 'ST'
        self.assertEqual(decrypted_text, expected)

if __name__ == "__main__":
    unittest.main()
