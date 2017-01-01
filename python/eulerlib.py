#
# Helper functions for Project Euler
# by Lucas Chen
#

import math


# Given integer n return whether n is prime.
# Source: https://en.wikipedia.org/wiki/Primality_test#Simple_methods
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True


# Given integer n, list the primes <= n.
def list_primes(n):
    return [i for i in range(1, n + 1) if is_prime(i)]


# Given integers n, k, compute the binomial coefficient, n choose k
def binomial(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
