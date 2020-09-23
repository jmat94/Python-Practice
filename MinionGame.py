def getHighestCount(string):

    """
    A program to check which player would win a match if player1 has substrings starting with vowels
    or if player2 has substrings starting with consonants
    """


    vowel_string = ['A', 'E', 'I', 'O', 'U']
    string_length = len(string)


    # Players
    kevin_count = 0
    stuart_count = 0


    for char in range(string_length):
        if(string[char] in vowel_string):
            kevin_count += (string_length - char)
        else:
            stuart_count += (string_length - char)

    if (kevin_count > stuart_count):
        print("Kevin " + str(kevin_count))
    elif(stuart_count > kevin_count):
        print("Stuart " + str(stuart_count))
    else:
        print("Draw")

getHighestCount("BANANA")