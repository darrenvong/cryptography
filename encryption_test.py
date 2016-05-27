# -*- coding: utf-8 -*-

"""
A set of unit tests for the encryption module's various encrpytion and decryption functions.
@author: Darren Vong
"""
import unittest

import numpy as np
from numpy.testing import assert_equal

import encryption
from encryption import (NUMS_TO_ALPHABET_MOD26, NUMS_TO_ALPHABET_MOD29,
                        ALPHABET_TO_NUMS_MOD26)

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
        M_inv = encryption.inverse_matrix(M, 29)
        expected = np.array([[16,19],[19,10]])
        assert_equal(M_inv, expected)

    def test_inv_3x3(self):
        M = np.array([[1,2,3],[0,2,1],[0,3,4]])
        M_inv = encryption.inverse_matrix(M, 7)
        expected = np.array([[1,3,2],[0,5,4],[0,5,6]])
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

    def test_convert_message(self):
        msg = np.array([15,11,20,12])
        converted_msg = encryption.convert_message(msg, NUMS_TO_ALPHABET_MOD26)
        expected = 'PLUM'
        self.assertEqual(converted_msg, expected)

    def test_convert_message_reversed(self):
        msg = 'PLUM'
        converted_msg = encryption.convert_message(msg, ALPHABET_TO_NUMS_MOD26, True)
        expected = np.array([15,11,20,12])
        assert_equal(converted_msg, expected)

    def test_vig_encrypt_even_len_msg(self):
        k = 'PLUM'
        m = np.array([18,4,11,11,0,11,11,14,20,17,18,7,0,17,4,18])
        encrypted = encryption.vigenere_encrypt(k, m)
        expected = 'HPFXPWFAJCMTPCYE'
        self.assertEqual(encrypted, expected)

    def test_vig_encrypt_odd_len_msg(self):
        k = 'PLUM'
        m = np.array([18,4,11,11,0,11,11])
        encrypted = encryption.vigenere_encrypt(k, m)
        expected = 'HPFXPWF'
        self.assertEqual(encrypted, expected)

    def test_vig_encrypt_key_with_space(self):
        k = 'PL UM'
        m = np.array([18,4,11,11,0])
        encrypted = encryption.vigenere_encrypt(k, m)
        expected = 'HPFXP'

    def test_vig_decrypt_even_len_msg(self):
        k = 'PLUM'
        m = np.array([9,0,13,19,19,13,11,16,19,21])
        decrypted = encryption.vigenere_decrypt(k, m)
        expected = 'UPTHECREEK'
        self.assertEqual(decrypted, expected)

    def test_vig_decrypt_odd_len_msg(self):
        k = 'PLUM'
        m = np.array([9,0,13])
        decrypted = encryption.vigenere_decrypt(k, m)
        expected = 'UPT'
        self.assertEqual(decrypted, expected)

    def test_vig_decrypt_key_with_space(self):
        k = 'PL U M'
        m = np.array([9,0,13,19,19,13])
        decrypted = encryption.vigenere_decrypt(k, m)
        expected = 'UPTHEC'
        self.assertEqual(decrypted, expected)

    def test_one_time_pad_encrypt(self):
        # This is effectively Vigenere encryption except key is a phrase rather
        # than periodic text, hence Vigenere should still work for this
        k = 'RERUM COGNOSCERE CAUSAS'
        m = np.array([6,4,19,14,20,19,19,14,13,8,6,7,19])
        encrypted = encryption.vigenere_encrypt(k, m)
        expected = 'XIKIGVHUAWYJX'
        self.assertEqual(encrypted, expected)

    def test_one_time_pad_decrypt(self):
        # Same reasoning in one_time_pad_encrypt applies for this
        k = 'RERUM COGNOSCERE CAUSAS'
        m = np.array([20,18,4,13,18,16,7,13,17,5,22])
        decrypted = encryption.vigenere_decrypt(k, m)
        expected = 'DONTGOTHERE'
        self.assertEqual(decrypted, expected)

    

if __name__ == "__main__":
    unittest.main()
