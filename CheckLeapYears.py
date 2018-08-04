def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

for year in range(1900, 2021):
    print(year, check_leap_year(year))

