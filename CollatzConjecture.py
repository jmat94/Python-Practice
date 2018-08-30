"""

This program is to generate the numbers obtained using collatz conjecture.

"""
# Define the function
def collatz_conjecture(num):
    seq = []
    count_of_steps = 0
    while num > 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = (3 * num) + 1

        # Counting the steps it takes to solve for a specific number
        count_of_steps += 1

        #appending the values to list
        seq.append(int(num))
    return seq, count_of_steps
        # return True
    # return False

# print("The numbber of steps are: ", collatz_conjecture(22))
print(collatz_conjecture(7))




