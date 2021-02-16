"""
Create a 2-dimensional array of n empty arrays. All arrays are zero indexed.
Create an integer 'lastAnswer 'and initialize it to 0.
There are  types of queries:
Query: 1 x y
Find the list within the 2D array at index idx = ((x ^ lastAnswer)) % n.
Append the integer y to the array[idx].
Query: 2 x y
Find the list within arr at index idx = ((x ^ lastAnswer) % n).
Find the value of element Y % len(array[idx])  where len is the number of elements in array[idx] and
assign the value to lastAnswer.
Print the new value of lastAnswer on a new line.
"""


def dynamicArray(n, queries):

    # Declaring a 2D array
    arraySequence = [[] for _ in range(n)]
    lastAnswer = 0
    finalAnswer = []

    for q in queries:

        # Idx is position of an array within the 2D array
        idx = (q[1] ^ lastAnswer) % n


        # Checking if it is query 1
        if (q[0] == 1):
            arraySequence[idx].append(q[2])

        else:

            # if it is query 2
            value = q[2] % len(arraySequence)
            lastAnswer = arraySequence[idx][value]
            finalAnswer.append(lastAnswer)

    return finalAnswer

if __name__ == '__main__':
    n_input = input().rstrip().split()

    n = int(n_input[0])

    q = int(n_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = dynamicArray(n, queries)

    print("\n".join(map(str, ans)))



