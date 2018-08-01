import time
import math

def check_prime(num):
    max_divisor = math.floor(math.sqrt(num))
    if num == 1:
        return False
    else:
        for i in range(2, max_divisor + 1):
            if num % i == 0:
                return False
        return True

t0 = time.time()
for i in range(2, 1000):
    print(check_prime(i))

t1 = time.time()

print("The time taken is: ", t1 - t0)























