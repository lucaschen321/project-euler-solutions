#
# Solution to Project Euler Problem 3
# by Lucas Chen
#
# Answer: 6857
#

import math
import eulerlib

NUM = 600851475143

# Computes the largest prime that is a factor of [NUM]. Algorithm returns the
# result if it is prime. Otherwise, divides out the lowest prime after each pass
def compute():
    ans = NUM
    for i in eulerlib.list_primes((int)(math.sqrt(ans))):
        if eulerlib.is_prime(ans):
            return ans
        while ans % i == 0 and ans != i:
           ans //= i

# Alternate solution: Computes prime factorization, and finding the maximum
# prime factor
'''
def compute():
    ans = NUM
    i = 2
    factors = []  # List of the prime factors for ans
    while i <= ans:
        while ans % i == 0:
            ans //= i
            factors.append(i)
        i += 1

    for j in factors:
        if j > ans:
            ans = j
    return ans
'''

if __name__ == "__main__":
    print(compute())
