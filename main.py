import math

entered_date = input('Enter a date: ')


def sum_date(date):
    return sum(int(x) for x in date if x.isdigit())


print('Factorial for the given date: ', math.factorial(sum_date(entered_date)))
