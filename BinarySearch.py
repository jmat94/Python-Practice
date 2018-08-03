def binary_search(arr, left, right, num):
    while left <= right:

        mid_element = int((left + right)/2)

        if arr[mid_element] > num:
            right = mid_element - 1
        elif arr[mid_element] < num:
            left = mid_element + 1
        else:
            return mid_element

     return -1

arr = [5, 10, 20, 40, 80]
num = 20

result = binary_search(arr, 0, len(arr)-1, num)

print(result)
