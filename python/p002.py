#
# Solution to Project Euler problem 2
# by Lucas Chen
#
# Answer: 4613732
#

NUM = 4000000

# Computes the sum of the even-valued terms in the Fibonacci sequence that are
# less than [NUM]
def compute():
    ans = 0
    x = 1  # The trailing fibonacci number
    y = 1  # The leading fibonacci number - the one being processed/added
    while  y < NUM:
        if  y % 2 == 0:
            ans += y
        x, y = y, y +x
    return ans

if __name__ == "__main__":
    print(compute())
