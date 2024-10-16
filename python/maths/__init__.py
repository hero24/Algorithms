from .sieve_eratosthenes import EratosthenesSieve, eratosthenes_sieve as Eratosthenes
from .sieve_sundaram import sundaram_sieve as Sundaram
from .fibonacci import *
from .functions import newton, linear_function_result, lagrange_interpolation
from .functions import simpson_integration
from .gauss import gauss
from .polynomials import polynomial_std, horner
from .polynomials import add as add_polynomials
from .polynomials import multiply as multiply_polynomials
"""
Always remember that you are absolutely unique. Just like everyone else.
-Margaret Mead
"""

__all__ = [
    "EratosthenesSieve",
    "Eratosthenes",
    "Sundaram",
    "fibonacci_recursive",
    "fibonacci_iterative",
    "fibonacci_memo",
    "fibonacci_dynamic",
    "newton",
    "linear_function_result",
    "lagrange_interpolation",
    "simpson_integration"
    "gauss",
    "add_polynomials",
    "multiply_polynomials",
    "polynomial_std",
    "horner"
]
