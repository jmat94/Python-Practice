"""
This program is used to find the difference between the min and max number(without using the inbuilt functions) after sorting the list
"""

# Define the function
def sort_and_find_big_diff(nums):

    # Create min and max variables
    min_num = nums[0]
    max_num = nums[0]

    # Sort the list
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    print("The sorted list is: {}".format(nums))

    # Find the minimum number
    for i in nums:
        if i < min_num:
            min_num = i

    # Find the max number
    for i in nums:
        if i > max_num:
            max_num = i

    # Find the difference between the min and max number
    print("The difference between the largest and smallest number is: {}".format(max_num - min_num))

sort_and_find_big_diff(nums=[10, 3, 5, 6])
