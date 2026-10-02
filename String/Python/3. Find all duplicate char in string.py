def printDups(str):
    count = {}

    # Count frequency of each character
    for i in range(len(str)):
        count[str[i]] = count.get(str[i], 0) + 1

    # Iterate through dictionary
    for char, freq in count.items():

        # If frequency is greater than 1, duplicate found
        if freq > 1:
            print(char, ", count =", freq)


# Driver code
str = "test string"

printDups(str)


'''
Time Complexity:
O(n)

Reason:

We traverse the string once to count the frequency
of every character.

Then we iterate through the dictionary.

In the worst case, the dictionary can contain up to n
different characters.

Therefore:
O(n)


Space Complexity:
O(n)

Reason:

We use a dictionary to store the frequency of characters.

In the worst case, every character in the string is unique,
so the dictionary can store up to n entries.

Therefore:
O(n)
'''