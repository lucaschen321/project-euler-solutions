#
# Solution to Project Euler Problem 14
# by Lucas Chen
#
# Answer: 837799
#

NUM = 1000000


# Compute the largest number less than [NUM] that produces the longest Collatz
# sequence
def compute():
    # Create a mapping from each integer, n where 0 < n < [NUM], to the length
    # of its Collatz squence
    collatz, length = {1: 1}, 1
    for i in range(1, NUM):
        num, length = i, 1
        # Add [i] to dictionary, if it is not in the mapping.
        while num not in collatz:
            if num % 2 == 0:
                num //= 2
            else:
                num = num * 3 + 1
            length += 1
        collatz[i] = length + collatz[num]
    # Return the key in the mapping with the maximum value
    return max(collatz, key=collatz.get)

if __name__ == "__main__":
    print(compute())
