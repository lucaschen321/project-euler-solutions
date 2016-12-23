#
# Solution to Project Euler problem 3
# by Lucas Chen
#
# Answer: 6857
#

import math
import eulerlib

# Algorithm divides out the lowest prime after each pass, and returns the 
# result if it is prime.
def compute():
    ans = 600851475143
    for i in eulerlib.list_primes((int)(math.sqrt(ans))):
        if eulerlib.is_prime(ans):
            return ans
        while ans % i == 0 and ans != i:
           ans //= i

# Alternate solution by computing prime factorization, and finding the maximum
# prime factor
'''
def compute():
    ans = 600851475143
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
