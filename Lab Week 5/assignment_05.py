# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.

from vec import Vec
from mat import Mat
from bitutil import bits2mat, str2bits, noise
from GF2 import one
from matutil import listlist2mat 


## Task 1
""" Create an instance of Mat representing the generator matrix G. You can use
the procedure listlist2mat in the matutil module (be sure to import first).
Since we are working over GF (2), you should use the value one from the
GF2 module to represent 1"""
g = [
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0],

]

A = listlist2mat()
G = A

## Task 2
# Please write your answer as a Vec. Use one from GF2 and 0 as the elements.
encoding_1001 = None


## Task 3
# Express your answer as an instance of the Mat class.
R = None

## Task 4
# Create an instance of Mat representing the check matrix H.
H = None

## Task 5
def find_error(syndrome):
    """
    Input: an error syndrome as an instance of Vec
    Output: the corresponding error vector e
    Examples:
        >>> find_error(Vec({0,1,2}, {0:one})) == Vec({0, 1, 2, 3, 4, 5, 6},{3: one})
        True
        >>> find_error(Vec({0,1,2}, {2:one})) == Vec({0, 1, 2, 3, 4, 5, 6},{0: one})
        True
        >>> find_error(Vec({0,1,2}, {1:one, 2:one})) == Vec({0, 1, 2, 3, 4, 5, 6},{2: one})
        True
        >>> find_error(Vec({0,1,2}, {})) == Vec({0,1,2,3,4,5,6}, {})
        True
    """
    pass

## Task 6
# Use the Vec class for your answers.
non_codeword = ...
error_vector = ...
code_word = ...
original = ...


## Task 7
def find_error_matrix(S):
    """
    Input: a matrix S whose columns are error syndromes
    Output: a matrix whose cth column is the error corresponding to the cth column of S.
    Example:
        >>> S = listlist2mat([[0,one,one,one],[0,one,0,0],[0,0,0,one]])
        >>> find_error_matrix(S) == Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}), {(1, 3): 0, (3, 0): 0, (2, 1): 0, (6, 2): 0, (5, 1): one, (0, 3): 0, (4, 0): 0, (1, 2): 0, (3, 3): 0, (6, 3): 0, (5, 0): 0, (2, 2): 0, (4, 1): 0, (1, 1): 0, (3, 2): one, (0, 0): 0, (6, 0): 0, (2, 3): 0, (4, 2): 0, (1, 0): 0, (5, 3): 0, (0, 1): 0, (6, 1): 0, (3, 1): 0, (2, 0): 0, (4, 3): one, (5, 2): 0, (0, 2): 0})
        True
    """
    pass

## Task 10
s = "I'm trying to free your mind, Neo. But I can only show you the door. You're the one that has to walk through it."
P = None

## Task 12
C = None
bits_before = None
bits_after = None


## Task 13 - ungraded
CTILDE = None

## Task 14
def correct(A):
    """
    Input: a matrix A each column of which differs from a codeword in at most one bit
    Output: a matrix whose columns are the corresponding valid codewords.
    Example:
        >>> A = Mat(({0,1,2,3,4,5,6}, {1,2,3}), {(0,3):one, (2, 1): one, (5, 2):one, (5,3):one, (0,2): one})
        >>> correct(A) == Mat(({0, 1, 2, 3, 4, 5, 6}, {1, 2, 3}), {(0, 1): 0, (1, 2): 0, (3, 2): 0, (1, 3): 0, (3, 3): 0, (5, 2): one, (6, 1): 0, (3, 1): 0, (2, 1): 0, (0, 2): one, (6, 3): one, (4, 2): 0, (6, 2): one, (2, 3): 0, (4, 3): 0, (2, 2): 0, (5, 1): 0, (0, 3): one, (4, 1): 0, (1, 1): 0, (5, 3): one})
        True
    """
    pass


## Task 15
def decode_with_error(A):
    """
    Input: a matrix A each column of which differs from a codeword in at most one bit
    Output: the original plaintext
    Example:
        >>> A = Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3, 4, 5}), {(0, 0): 0, (1, 0): 0, (2, 0): one, (3, 0): 0, (4, 0): one, (5, 0): one, (6, 0): 0, (0, 1): one, (1, 1): 0, (2, 1): 0, (3, 1): one, (4, 1): one, (5, 1): 0, (6, 1): 0, (0, 2): 0, (1, 2): one, (2, 2): 0, (3, 2): 0, (4, 2): one, (5, 2): 0, (6, 2): one, (0, 3): one, (1, 3): one, (2, 3): 0, (3, 3): 0, (4, 3): one, (5, 3): one, (6, 3): 0, (0, 4): one, (1, 4): one, (2, 4): one, (3, 4): one, (4, 4): one, (5, 4): one, (6, 4): one, (0, 5): one, (1, 5): one, (2, 5): 0, (3, 5): 0, (4, 5): one, (5, 5): one, (6, 5): 0})
        >>> decode_with_error(A)
        'Neo'
    """
    pass
