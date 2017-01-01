#
# Solution to Project Euler Problem 15
# by Lucas Chen
#
# Answer: 137846528820
#

import eulerlib

NUM = 20


# Compute the number of routes in a [NUM] x [NUM] grid from the top left corner
# to the bottom right corner, while only being able to move to the right and
# down. This is equivalent to calculating the number of permutations of a
# string with [NUM] "R"'s and [NUM] "D"'s. Mathemtically, this is
# [NUM * 2] choose [NUM]
def compute():
    ans = eulerlib.binomial(NUM * 2, NUM)
    return ans

if __name__ == "__main__":
    print(compute())
