# Solution to Project Euler Problem 20
# by Lucas Chen
#
# Answer: 648
#

import math

NUM = 100


# Compute sum of digits of [NUM] factorial
def compute():
    return sum(map(int, str(math.factorial(100))))


if __name__ == "__main__":
    print(compute())
