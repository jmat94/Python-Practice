def stringAnagrams(listWithStringsToCompare, stringList):
	
	"""
		Function to check if anagrams exist in two lists containing strings
		
		Parameters:
		
				listWithStringsToCompare - A list of strings

				stringList - A list of strings

		Returns - A list containg indices of anagrams that exist in the two lists

	"""
    
    # Initializing an empty list
    indexList = []

    for string in range(len(listWithStringsToCompare)):


    	# A dictionary that contains count of each character of each string
        queryCharCount = {c: listWithStringsToCompare[query].count(c) for c in listWithStringsToCompare[query]}

        for word in range(len(stringList)):

        	# A dictionary that contains count of each character of each string
            wordCharCount = {c: stringList[word].count(c) for c in stringList[word]}

            # Comparing character counts
            if wordCharCount == queryCharCount:

                indexList.append(word)


    return indexList


listWithStringsToCompare = ["narc", "a", "khar", "abc"]

stringList = ["obs", "carn", "by", "racn"]


print(stringAnagrams(listWithStringsToCompare, stringList))






