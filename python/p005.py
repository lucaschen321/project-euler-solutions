#
# Solution to Project Euler Problem 5
# by Lucas Chen
#
# Answer: 232792560
#

import fractions
import eulerlib

NUM = 20   # The largest integer, for which the answer is evenly divsiible all
           # naturals less than [NUM]

# Using a loop, performs a fold with multiplication as the operator on naturals
# up to and including [NUM]. The greatest common divisor between the accumulator
# and the element of interest is divided out.
def compute():
    ans = 1
    for x in range(1, NUM + 1):
        if ans % x != 0:
            ans *= x // fractions.gcd(x, ans)
    return ans

# Alternate solution: Returns the list of primes less than or including [NUM]. 
# For each prime, the largest power of the prime less than or equal to [NUM] is 
# computed. The resulting powers are multiplied to give the answer.
''' 
def compute():
    ans = 1
    for x in eulerlib.list_primes(NUM):
        factor = x
        while factor < NUM:
            factor = factor * x
        ans *= factor // x
    return ans
'''

if __name__ == "__main__":
    print(compute())
