def getSubString(string, num):

    """
    Split a string in k contiguous blocks if the k is a factor of the length of the string

    :param string: A string
    :param num: Creating subsets of the string of size num
    :return: Strings of size num
    """


    temp_value = 0
    new_arr = []

    for value in string:
        temp_value += 1
        if value not in new_arr:
            new_arr.append(value)
        if temp_value == num:
            print("".join(new_arr))
            new_arr = []
            temp_value = 0

getSubString("AABCAAADAA", int(input()))
