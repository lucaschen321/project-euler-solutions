# Solution to Project Euler Problem 16
# by Lucas Chen
#
# Answer: 1366
#

POWER = 1000


# Computes 2 raised to the [POWER]th power, and returns the sum of the digits.
def compute():
    ans = 0
    num = 2 ** POWER
    while num > 0:
        # Add last digit to existing sum and remove it from number being
        # processed
        ans += num - num // 10 * 10
        num //= 10
    return ans

if __name__ == "__main__":
    print(compute())
