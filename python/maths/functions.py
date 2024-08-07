"""
"Mathematics may not teach us how to add love or subtract hate,
but it gives us every reason to hope that every problem has a solution."
 ~ Anonymous.
"""

EPSILON = 0.0001


def newton(x, func, fst_dirrivative):
    """
    finds function 0 spots
    """
    if abs(func(x)) < EPSILON:
        return x
    else:
        return newton(x - func(x) / fst_dirrivative(x), func, fst_dirrivative)


def linear_function_result(x, n):
    """
    finds function value
    """
    y = 2 * n - x * n * n
    if abs(n-y) < EPSILON:
        return y
    else:
        return linear_function_result(x, y)


def lagrange_interpolation(z, x, y):
    """
    Lagrange method function interpolation
    """
    wnz = 0
    om = 1
    n = min(len(x),len(y))
    for i in range(n):
        om = om * (z-x[i])
        w = 1.0
        for j in range(n):
            if i != j:
                w = w * (x[i]-x[j])
                wnz = wnz + y[i]/(w*(z-x[i]))
    return wnz * om


def simpson_integration(func, a, b, n):
    """
    simpsons method of integration of function
    """
    s = 0
    h = (b - a) / n
    for i in range(1,n):
        s += h * (func(a + (i-1) * h) + 4 * func(a-h/2.0+i*h) + func(a+i*h))/6.0
    return s
