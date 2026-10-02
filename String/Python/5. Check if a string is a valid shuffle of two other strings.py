def isValidShuffle(s1, s2, shuffled):
    # Check if the lengths match
    if len(shuffled) != len(s1) + len(s2):
        return False

    # Pointers for s1 and s2
    i = 0
    j = 0

    # Iterate through each character in shuffled string
    for c in shuffled:

        # Check if character can come from s1
        if i < len(s1) and c == s1[i]:
            i += 1

        # Check if character can come from s2
        elif j < len(s2) and c == s2[j]:
            j += 1

        # Character does not match either string
        else:
            return False

    # Check if both strings are completely used
    return i == len(s1) and j == len(s2)


# Example
s1 = "abc"
s2 = "123"
shuffled = "a1b2c3"

if isValidShuffle(s1, s2, shuffled):
    print("The string is a valid shuffle of the two strings.")
else:
    print("The string is not a valid shuffle of the two strings.")


'''
Time Complexity:
O(n + m)

Reason:

We traverse the shuffled string once.

The length of shuffled is:
n + m

where:
n = length of s1
m = length of s2

Therefore:
O(n + m)


Space Complexity:
O(1)

Reason:

We only use two pointers:
i and j

No extra data structure is used.

Therefore:
O(1)
'''