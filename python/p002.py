#
# Solution to Project Euler problem 2
# by Lucas Chen
#
# Answer: 4613732
#

def compute():
    ans = 0
    x = 1  # The smaller fibonacci number
    y = 1  # The larger fibonacci number - the one being processed
    while  y < 4000000:
        if  y % 2 == 0:
            ans += y
        x , y = y, y +x
    return ans

if __name__ == "__main__":
    print(compute())
