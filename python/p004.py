#
# Solution to Project Euler problem 4
# by Lucas Chen
#
# Answer: 906609
#

# Computes the largest palindrome that is a product of two 3-digit numbers
def compute():
    ans = 0
    for x in range(100, 1000):
        for y in range(100, 1000):
            if x * y > ans and str(x*y) == str(x*y)[::-1]:
                ans = x * y
    return ans

if __name__ == "__main__":
    print(compute())
