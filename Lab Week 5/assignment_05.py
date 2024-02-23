# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.

from vec import Vec
from mat import *
from bitutil import *
from GF2 import one
from matutil import *


## Task 1
""" Create an instance of Mat representing the generator matrix G. You can use
the procedure listlist2mat in the matutil module (be sure to import first).
Since we are working over GF (2), you should use the value one from the
GF2 module to represent 1"""
g = [
    [one, 0, one, one], 
    [one, one, 0, one], ## [1, 0, 0, 1]
    [0, 0, 0, one],
    [one, one, one, 0],
    [0, 0, one, 0],
    [0, one, 0, 0],
    [one, 0, 0, 0]
]

A = listlist2mat(g)
G = A
# >>> Comlete


## Task 2
# Please write your answer as a Vec. Use one from GF2 and 0 as the elements.

## [1, 0, 0, 1]
[0, 0, one, one, 0, 0, one]
v = Vec({0, 1, 2, 3, 4, 5, 6}, {2: one, 3:one, 6: one })

# print(v)

encoding_1001 = None
# einfeldið. þetta er yfir GF(2)


# >>> Comlete

## Task 3
# Express your answer as an instance of the Mat class.
## Finna R fylkið þannig að R * G gefur okkur Hlutlaust-Fylki/Eininga-Fylki
## R er 4*7, og G er 7*4.
# í Raun erum við að finna R ° G, sem gefur okkur hlutlausa fylkið.

r = [
    [0, 0, 0, 0, 0, 0, one],
    [0, 0, 0, 0, 0, one, 0],
    [0, 0, 0, 0, one, 0, 0],
    [0, 0, one, 0, 0 ,0, 0],
]
r_mat = listlist2mat(r)
R = r_mat
# >>> Comlete

"""In such a code, there is a matrix H, called the check matrix, such that C is the null space of H. When the Receiver receives the vector c ̃, she can check whether the received vector is a codeword by multiplying it by H and checking whether the resulting vector (called the error syndrome) is the zero vector."""
## Task 4
# Create an instance of Mat representing the check matrix H.
h = [
    [0, 0, 0, one, one, one, one],
    [0, one, one, 0, 0, one, one],
    [one, 0, one, 0, one, 0, one]]

g = listlist2mat(h)

H = g
# -> þetta virkar ekki alveg, en finnst þetta bara vera fín byrjun marh. 
#hg = 0
# Complete
print(H)
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
    """result = {}
    for lis in h: 
        for item in lis:
            for val in syndrome.f:
                new_var = item * val
                result += {new_var}"""
    new_mat = mat2coldict(H)
    counter = 0 
    for col in new_mat:
        counter += 1 
        if new_mat[col] == syndrome:
            ret_syndrome = Vec({0, 1, 2, 3, 4, 5, 6}, {counter -1: one})
    return ret_syndrome
            

#find_error(Vec({0,1,2}, {0:one})) == Vec({0, 1, 2, 3, 4, 5, 6},{3: one})
# find_error(Vec({0,1,2}, {2:one})) == Vec({0, 1, 2, 3, 4, 5, 6},{0: one})

"""find_error(Vec({0,1,2}, {0:one})) == Vec({0, 1, 2, 3, 4, 5, 6},{3: one})

find_error(Vec({0,1,2}, {2:one})) == Vec({0, 1, 2, 3, 4, 5, 6},{0: one})

find_error(Vec({0,1,2}, {1:one, 2:one})) == Vec({0, 1, 2, 3, 4, 5, 6},{2: one})

find_error(Vec({0,1,2}, {})) == Vec({0,1,2,3,4,5,6}, {})"""

# >>> Complete

## Task 6
# Use the Vec class for your answers.


non_codeword = Vec({0, 1, 2, 3, 4, 5, 6}, {0:one, 2:one, 3:one, 5:one, 6:one})
# e = find_error(Vec({0,1,2}, {0:one, 1:one, 2:one}))
# error_vector = e
error_vector = Vec({0, 1, 2, 3, 4, 5, 6}, {6:one})
# code_word = e + non_codeword
code_word = Vec({0, 1, 2, 3, 4, 5, 6}, {0:one, 2:one, 3:one, 5:one})
print(code_word)
# original = R * code_word
original = Vec({0, 1, 2, 3}, {1:one, 3:one})
print(original)

# Complete

## Task 7
def find_error_matrix(S):
    # error vigrarnir eru 7 á lengd niður. 

    
    """
    Input: a matrix S whose columns are error syndromes
    Output: a matrix whose cth column is the error corresponding to the cth column of S.
    Example:
        >>> S = listlist2mat([[0,one,one,one],[0,one,0,0],[0,0,0,one]])
        >>> find_error_matrix(S) == Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}), {(1, 3): 0, (3, 0): 0, (2, 1): 0, (6, 2): 0, (5, 1): one, (0, 3): 0, (4, 0): 0, (1, 2): 0, (3, 3): 0, (6, 3): 0, (5, 0): 0, (2, 2): 0, (4, 1): 0, (1, 1): 0, (3, 2): one, (0, 0): 0, (6, 0): 0, (2, 3): 0, (4, 2): 0, (1, 0): 0, (5, 3): 0, (0, 1): 0, (6, 1): 0, (3, 1): 0, (2, 0): 0, (4, 3): one, (5, 2): 0, (0, 2): 0})
        True
    """
    """Write a one-line procedure find_error_matrix with the following spec:
            • input: a matrix S whose columns are error syndromes
            • output: a matrix whose cth column is the error corresponding to the cth column of S.
        This procedure consists of a comprehension that uses the procedure find_error together with some procedures from the matutil module.
        Test your procedure on a matrix whose columns are [1, 1, 1] and [0, 0, 1]."""
    return coldict2mat({col: find_error(mat2coldict(S)[col]) for col in S.D[1]})

S = listlist2mat([[0,one,one,one],[0,one,0,0],[0,0,0,one]])


## Task 10
s = "I'm trying to free your mind, Neo. But I can only show you the door. You're the one that has to walk through it."
sp = str2bits(s)
P = sp

## Task 12
P = bits2mat(P, 7)
C = matrix_matrix_mul(g, P)
print(C)
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
