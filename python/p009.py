#
# Solution to Project Euler Problem 9
# by Lucas Chen
#
# Answer: 31875000
#

NUM = 1000

# A Pythagorean triplet is defined as a set of natural numbers a < b < c such 
# that a^2 + b^2 = c^2. Finds a Pythogorean triplet such that a + b + c = [NUM]
# and returns product abc, and -1 if a triplet is not found. Fewer numbers 
# checked by looping such that a < b < c.
def compute():
    for c in range(NUM):
        for b in range(c):
            for a in range(b):
                if a + b + c == NUM and a ** 2 + b ** 2 == c ** 2:
                    return a * b * c
    return -1

if __name__ == "__main__":
    print(compute())
