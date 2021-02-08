def rotateArrayToTheLeftByOne(arr, arr_length):
	"""
		Function to move values to the left by one
		
		Parameters: 

				arr - An array of integers
				arr_length - Length of the array
	"""
	
	temp_value = arr[0]

	for num in range(arr_length - 1):
	
		arr[num] = arr[num + 1]

	arr[arr_length - 1] = temp_value


def rotateArrayByNValue(arr, rotationValue, arr_length):
	"""
		
		Function to move values in an array to the left by a specific value

		Parameters: 

				arr - An array of integers
				rotationValue - A value to rotate the array by
				arr_length - Length of the array
	"""

	for num in range(rotationValue):
		rotateArrayToTheLeftByOne(arr, arr_length)

arr = [1,2,3,4,5,6]

arr_length = len(arr)

rotateArrayByNValue(arr, 2, arr_length)


for i in arr:
	print(i, end = " ")


