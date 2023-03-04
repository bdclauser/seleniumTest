def is_leap_year(year):
    # if the year is divisible by 4 and not divisible by 100, or
    # if the year is divisible by 400 then the year is a leap year, return `True`
    # otherwise return `False`
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
