#
# Solution to Project Euler Problem 7
# by Lucas Chen
#
# Answer: 104743
#

import eulerlib

NUM = 10001

# Compute the first [NUM] primes,storing them in a list, and returns the
# [NUM]th prime
def compute():
    primes, i = [], 1
    while len(primes) < NUM:
        if eulerlib.is_prime(i):
            primes.append(i)
        i += 1
    return primes[NUM - 1]

if __name__ == "__main__":
    print(compute())
