#
# Solution to Project Euler Problem 10
# by Lucas Chen
#
# Answer: 142913828922
#

import eulerlib

NUM = 2000000

# Computes the sum of all the primes less than [NUM]
def compute():
    return sum(eulerlib.list_primes(NUM - 1))

if __name__ == "__main__":
    print(compute())
