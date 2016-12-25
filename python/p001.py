#
# Solution to Project Euler Problem 1
# by Lucas Chen
#
# Answer: 233168
#

NUM = 1000


# Compute sum of the naturals that are a multiple of 3 or 5 and less than [NUM]
def compute():
    return sum(i for i in range(1, NUM) if i % 3 == 0 or i % 5 == 0)


if __name__ == "__main__":
    print(compute())
