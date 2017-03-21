# Solution to Project Euler Problem 17
# by Lucas Chen
#
# Answer: 21124
#

NUM = 1000


# Computes the number of letters used to write out 1 to [NUM] in words
def compute():
    str_ans = ""
    num_to_word = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
                   6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
                   11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
                   15: "fifteen", 16: "sixteen", 17: "seventeen",
                   18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
                   40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
                   80: "eighty", 90: "ninety", 100: "hundred",
                   1000: "thousand"}

    # Append the english representation of each number from 1 to [NUM]
    # to [str_ans]. Return the length of [str_ans]
    for i in range(1, NUM + 1):
        # In each successive if statement, replace all but the first digit with
        # 0's, convert the result to English, and then return [i] with the
        # first digit stripped to the next if statement.
        if 1000 <= i <= 9999:
            str_ans += num_to_word[i // 1000] + num_to_word[1000]
            i %= 1000
        if 100 <= i <= 999:
            str_ans += num_to_word[i // 100] + num_to_word[100]
            str_ans += "and" if i % 100 != 0 else ""
            i %= 100
        if 21 <= i <= 99:
            str_ans += num_to_word[i - i % 10]
            i %= 10
        if 1 <= i <= 20:
            str_ans += num_to_word[i]
    return len(str_ans)


if __name__ == "__main__":
    print(compute())
