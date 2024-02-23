from vec import Vec


def vec_select(veclist, k):
    """
    Returns a list of vectors from veclist where the value of entry k is 0.

    Args:
    - veclist: A list of Vec objects
    - k: A key value to be checked in the entries of the Vec objects

    Returns:
    - A list of Vec objects from veclist where the value of entry k is 0
    """
    result = []
    for vec in veclist:
        if k not in vec.f or vec[k] == 0:
            result.append(vec)
    return result

def vec_sum(veclist, D):
    """
    Returns the sum of all vectors in veclist.

    Args:
    - veclist: A list of Vec objects
    - D: The domain of the Vec objects

    Returns:
    - A Vec object representing the sum of all vectors in veclist
    """
    result_dict = {}
    for vecs in veclist:
        for key in vecs.f:
            if key in result_dict:
                result_dict[key] += vecs.f[key]
            else:
                result_dict[key] = vecs.f[key]
    return Vec(D, result_dict)

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
    return vec_sum(vec_select(veclist, k), D)

def scale_vecs(vecdict):
    """
    Returns a list of scaled versions of the vectors in vecdict.

    Args:
    - vecdict: A dictionary mapping scalar values to Vec objects

    Returns:
    - A list of scaled versions of the vectors in vecdict
    """
    result = []
    for key in vecdict:
        result.append((1/key) * vecdict[key])
    return result


## 3: (Problem 3.8.3) Constructing a Span over GF(2)

# def GF2_span(D, L):
    """
    Returns the span of the vectors in L over the field GF(2).

    Args:
    - D: The domain (a set)
    - L: A list of Vec objects

    Returns:
    - A list of Vec objects representing the span of the vectors in L over GF(2)
    """
    from itertools import product  # Import the product function from itertools
    from GF2 import one  # Import the one value from GF2 module

    # Helper function to compute linear combination of vectors
    def linear_combination(vectors, coefficients):
        return sum(Vec(D, {key: coeff for key, coeff in zip(vec.D, coefficients)}) for vec, coeff in zip(vectors, coefficients))

    # List to store the linear combinations
    result = []

    # Loop over all possible combinations of coefficients
    for coeffs in product([0, 1], repeat=len(L)):
        result.append(linear_combination(L, coeffs))

    return result
