#
# Solution to Project Euler Problem 6
# by Lucas Chen
#
# Answer: 25164150
#

NUM = 100

# Computes the difference between the sum of the squares of the first [NUM]
# natural numbers and the square of their sum.
def compute():
    sum_of_squares = sum(i ** 2 for i in range(1, NUM + 1))
    square_of_sums = sum(i for i in range (1, NUM + 1)) ** 2
    return square_of_sums - sum_of_squares

if __name__ == "__main__":
    print(compute())
