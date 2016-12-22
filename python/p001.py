#
# Solution to Project Euler problem 1
# by Lucas Chen
#
# Answer: 233168
#

def compute():
    return sum(i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0)

if __name__ == "__main__":
    print(compute())
