from vec import Vec
from GF2 import one

## 1: (Problem 3.8.1) Vector Comprehension and Sum
def vec_select(veclist, k):
    """
    Returns a list of vectors from veclist where the value of entry k is 0.

    Args:
    - veclist: A list of Vec objects
    - k: A key value to be checked in the entries of the Vec objects

    Returns:
    - A list of Vec objects from veclist where the value of entry k is 0
    """
    return [vec for vec in veclist if vec[k] == 0]

def vec_sum(veclist, D):
    """
    Returns the sum of all vectors in veclist.

    Args:
    - veclist: A list of Vec objects
    - D: The domain of the Vec objects

    Returns:
    - A Vec object representing the sum of all vectors in veclist
    """
    result = Vec(D, {})  # Nýr tómur vigur til að halda utan um summu vigranna
    for vec in veclist:
        result += vec  # Bætum við hvern vigur í veclist við niðurstöðuvigurinn
    return result

def vec_select_sum(veclist, k, D):
    """
    Returns the sum of all vectors in veclist where the value of entry k is 0.

    Args:
    - veclist: A list of Vec objects
    - k: A key value to be checked in the entries of the Vec objects
    - D: The domain of the Vec objects

    Returns:
    - A Vec object representing the sum of all vectors in veclist where the value of entry k is 0
    """
    selected_vectors = vec_select(veclist, k)  # Veljum vigrana sem uppfylla skilyrðið
    return vec_sum(selected_vectors, D)  # Skilum summu þeirra


## 2: (Problem 3.8.2) Vector Dictionary
def scale_vecs(vecdict):
    """
    Returns a dictionary with scaled versions of the vectors in vecdict.

    Args:
    - vecdict: A dictionary mapping scalar values to Vec objects

    Returns:
    - A dictionary with scaled versions of the vectors in vecdict
    """
    result = {}  # Nýr tómur orðabók til að halda utan um sköluðu vigrana
    for scalar, vec in vecdict.items():
        scaled_vec = Vec(vec.D, {key: val / scalar for key, val in vec.f.items()})  # Skulum niður vigtina með skalarinum
        result[scalar] = scaled_vec  # Bætum við sköludu vigtinni í niðurstöðuorðabókina
    return result


## 3: (Problem 3.8.3) Constructing a Span over GF(2)
def GF2_span(D, L):
    """
    Returns the span of the vectors in L over the field GF(2).

    Args:
    - D: The domain (a set)
    - L: A list of Vec objects

    Returns:
    - A list of Vec objects representing the span of the vectors in L over GF(2)
    """
    from GF2 import one  # Import the one value from GF2 module

    # Helper function to compute linear combination of vectors
    def linear_combination(vectors, coefficients):
        return sum(Vec(D, {key: coeff for key, coeff in zip(vec.D, coefficients)}) for vec, coeff in zip(vectors, coefficients))

    # List to store the linear combinations
    result = []

    # Loop over all possible combinations of coefficients
    for i in range(2 ** len(L)):
        coefficients = [(i >> j) & 1 for j in range(len(L))]
        result.append(linear_combination(L, coefficients))

    return result
