def binary_search(arr, left, right, num):
    while left <= right:

        mid = int(left + (right - left)/2)

        if arr[mid] > num:
            right = mid - 1
        elif arr[mid] < num:
            left = mid + 1
        else:
            return mid





    return -1

arr = [1,2,3,4,5]
num = 5

result = binary_search(arr, 0, len(arr)-1, num)

print(result)