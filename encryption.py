# -*- coding: utf-8 -*-

"""
Raw implementation of the cryptography encryption functions as taught in MAS345,
written as another mean to consolidate understanding of the concepts in the maths module.
@author: Darren Vong
"""
import itertools

import numpy as np
from numpy.linalg import det

"""Standard alphanumeric conversion dictionaries (tables) for mod 26 and mod 29"""
NUMS_TO_ALPHABET_MOD26 = ''.join([chr(i) for i in xrange(65,91)]) # 'A' starts at index 65 in ASCII in Python
ALPHABET_TO_NUMS_MOD26 = dict([(l, k) for k, l in enumerate(NUMS_TO_ALPHABET_MOD26)])

NUMS_TO_ALPHABET_MOD29 = ''.join([chr(i) for i in xrange(65,91)])+'_?!'
ALPHABET_TO_NUMS_MOD29 = dict([(l, k) for k, l in enumerate(NUMS_TO_ALPHABET_MOD29)])

def convert_message(m, table, reverse=False):
    """Converts a numeric message m into its alphabetical representation. table is
    the alphanumeric conversion dictionary between a message's numeric encoding and
    alphabetical representation, depending on if reverse is True; if it is,
    then converts an alphabetical message back to its numeric encoding instead."""
    
    if not reverse:
        message_in_letters = ''.join([table[l] for l in m])
        return message_in_letters
    else:
        if not isinstance(table.keys()[0], str):
            raise TypeError("Wrong type of conversion dictionary supplied.")
        message_in_nums = [table[i] for i in m]
        return message_in_nums

def caesar_encrypt(k, m, mod=26):
    encrypted_m = (m + k) % mod
    return convert_message(encrypted_m, NUMS_TO_ALPHABET_MOD26)

def caesar_decrypt(k, m, mod=26):
    decrypted_m = (m - k) % mod
    return convert_message(decrypted_m, NUMS_TO_ALPHABET_MOD26)

def affine_encrypt(K, L, m, table, mod=29):
    """Performs an n-dimensional affine encryption on a message m given a nxn matrix K
    and a nx1 column vector L. mod is the field in which the encryption is working in,
    which should be in mod 26 or 29. table is the alphanumeric conversion dictionary from
    the numerical encoding to the alphabetical representation of the message.
    Returns the encrypted message in letters."""

    encrypted_m = (np.dot(K,m) + L) % mod
    return convert_message(encrypted_m, table)

def affine_decrypt(K, L, m, table, mod=29):
    """The inverse operation of affine_encrypt: the paramaters have exactly the same
    meanings."""

    # This is going to be quite involved as numpy doesn't do inverse in fields,
    # don't really have time to do this for general n x n matrices so only works
    # for simple 2x2 for now...
    K_inv = inverse_2x2_matrix(K, mod)
    decrypted_m = (np.dot(m, K_inv) - np.dot(L, K_inv)) % mod
    return convert_message(decrypted_m, table)

def find_inverse(x, mod):
    """Find the inverse of x in mod 'mod' - e.g. 3^-1 in F_31 is -10 or 21"""
    for i in itertools.count(start=1):
        if (i * x) % mod == 0:
            return -1
        elif (i * x) % mod == 1:
            return i

def inverse_2x2_matrix(matrix, mod):
    inv_matrix = matrix.copy()
    inv_matrix[0,0], inv_matrix[1,1] = inv_matrix[1,1], inv_matrix[0,0]
    inv_matrix[0,1] *= -1
    inv_matrix[1,0] *= -1
    det_inv = find_inverse(int(det(matrix)), mod)
    return (det_inv * inv_matrix) % mod
