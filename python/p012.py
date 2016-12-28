#
# Solution to Project Euler Problem 12
# by Lucas Chen
#
# Answer: 76576500
#

import math

NUM = 500


# Compute the value of the first triangle number to have over [NUM] divisors
def compute():
    inc, num_factors = 1, 0
    ans = 0
    while num_factors <= 500:
        num_factors = compute_num_factors(ans)
        if num_factors > NUM:
            return ans
        ans += inc
        inc += 1
    return ans


# Returns the number of distinct factors of [n]
def compute_num_factors(n):
    factors = 0
    sqrt = int(math.sqrt(n))
    for i in range(1, sqrt):
        if n % i == 0:
            factors += 2
    if sqrt ** 2 == n:
        factors += 1
    return factors

if __name__ == "__main__":
    print(compute())
