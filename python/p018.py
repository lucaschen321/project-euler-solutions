# Solution to Project Euler Problem 18
# by Lucas Chen
#
# Answer: 1074
#


triangle_str = """ 75
                   95 64
                   17 47 82
                   18 35 87 10
                   20 04 82 47 65
                   19 01 23 75 03 34
                   88 02 77 73 07 63 67
                   99 65 04 28 06 16 70 92
                   41 41 26 56 83 40 80 70 33
                   41 48 72 33 47 32 37 16 94 29
                   53 71 44 65 25 43 91 52 97 51 14
                   70 11 33 28 77 73 17 78 39 68 17 57
                   91 71 52 38 17 14 91 43 58 50 27 29 48
                   63 66 04 68 89 53 67 30 73 16 69 87 40 31
                   04 62 98 27 23 09 70 98 73 93 38 53 60 04 23 """

# Preprocess string input so that each row is stored in an array
triangle = triangle_str.split('\n')
for i in range(len(triangle)):
    triangle[i] = list(map(int, triangle[i].strip().split()))

# Use dynamic programming to compute max path. Loop through each row,
# tabulating the maximum path to each index in some auxiliary array, max_path

max_path = [triangle[0][0]]

for i in range(1, len(triangle)):
    max_row = list(map(max, zip(max_path + [0], [0] + max_path)))
    max_path = list(map(sum, zip(max_row, triangle[i])))

if __name__ == "__main__":
    print(max(max_path))
