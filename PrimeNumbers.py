# Finding prime numbers using the method of finding the maximum divisor of the number to reduce the time taken.

import time
import math

# Creating the function 
def check_prime(num):
    # This line code finds the maximum divisor of the number
    max_divisor = math.floor(math.sqrt(num))
    
    if num == 1:
        return False
    else:
        for i in range(2, max_divisor + 1):
            if num % i == 0:
                return False
        return True

# Testing the function for the first 1000 numbers and checking the time taken.
t0 = time.time()
for i in range(2, 1000):
    print(check_prime(i))

t1 = time.time()

print("The time taken is: ", t1 - t0)























