from .sieve_eratosthenes import EratosthenesSieve, eratosthenes_sieve as Eratosthenes
from .sieve_sundaram import sundaram_sieve as Sundaram
from .fibonacci import *
from .functions import newton, linear_function_result, lagrange_interpolation, simpson_integration
from gauss import gauss
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
    "gauss"
]
