# This is program to find the leap years from 1900 to 2020. A leap year is a year that is divisible by 4 if it is 
# not divisible by 100 but divisible by 400.

# Function to find leap year
def check_leap_year(year):
    # Checking if the year is is divisible by 4 if it is not divisible by 100 but divisible by 400. 
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
    
# Checking all the leap years from 1900 to 2020.
for year in range(1900, 2021):
    print(year, check_leap_year(year))

