"""

This program is to generate the numbers obtained using collatz conjecture.

"""
# Define the function
def collatz_conjecture(num):
    seq = []
    count_of_steps = 0
    # We should continue the process till the number is greater than or equal to 1
    while num > 1:
        # If the number is even divide by 2
        if num % 2 == 0:
            num = num / 2
        else:
        # If the number is odd multiply it by 3 and add 1
            num = (3 * num) + 1

        # Counting the steps it takes to solve for a specific number
        count_of_steps += 1

        # Appending the values to list
        seq.append(int(num))
    return seq, count_of_steps
        # return True
    # return False

# print("The numbber of steps are: ", collatz_conjecture(22))
print(collatz_conjecture(7))




