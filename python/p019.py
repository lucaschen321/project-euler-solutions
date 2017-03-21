# Solution to Project Euler Problem 19
# by Lucas Chen
#
# Answer: 171
#


# Compute number of days in [month], given [month] and [year]
def numDays(month, year):
    numDays = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30,
               10: 31, 11: 30, 12: 31}
    if (month == 2 and
            ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)):
        return 29
    else:
        return(numDays[month])


# Compute number of Sundays that fell on the first of the month during the 20th
# century
def compute():
    # start on January 1st, 1901 - a Tuesday
    count = 0
    weekday = 2
    day = 1
    month = 1
    year = 1901
    while (year < 2001):
        # increment count if it is Sunday and first day of month
        if (weekday % 7 == 0 and day == 1):
            count += 1

        # increment day
        if (month == 12 and day == 31):
            weekday += 1
            day = 1
            month = 1
            year += 1
        elif (day == numDays(month, year)):
            weekday += 1
            day = 1
            month += 1
        else:
            weekday += 1
            day += 1
    return count


if __name__ == "__main__":
    print(compute())
