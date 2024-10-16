"""
"I had a polynomial once. My doctor removed it."
~ Michael Grant, Gone
"""

def polynomial_std(x, lst):
    """
    standard polynomial solver for polynomials
    represented in a list
    """
    result = 0
    pwr = 1
    for i in range(len(lst)-1, -1, -1):
        result += pwr * lst[i]
        pwr *= x
    return result


def horner(x, lst):
    """
    standard polynomial solver using Horners
    method for polynomials represented in a list
    """
    result = lst[0]
    for i in range(1, len(lst)):
        result = result * x + lst[i]
    return result


def add(x, y):
    """
    add polynimials represented as lists
    """
    z = []
    for i in range(min(len(x), len(y))):
        z.append(x[i] + y[i])
    return z


def multiply(x, y):
    """
    multuply polynomials represented as lists
    """
    rng = min(len(x),len(y))
    z = [0 for _ in range(rng)]
    for i in range(rng):
        for j in range(rng):
            z[i+j] = z[i+j] + x[i] * y[j]
    return z