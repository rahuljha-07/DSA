# To solve the problem of splitting a binary string into the maximum number of consecutive
# substrings with an equal number of 0s and 1s, we can follow these steps:
# Initialize Counters: We'll maintain a count of 0s and 1s as we iterate through the string.
# Count Balanced Substrings: Every time the counts of 0s and 1s are equal, we can conclude
# that we have found a balanced substring. We'll increment a counter to keep track of the
# number of such substrings.
# Check for Imbalance: If we reach the end of the string and have not seen a balanced count,
# we can conclude that splitting is impossible.
def maxBalancedSubstrings(str):
    count0 = 0
    count1 = 0
    maxCount = 0

    # Iterate through the binary string
    for ch in str:

        if ch == '0':
            # Increment count of 0s
            count0 += 1

        else:
            # Increment count of 1s
            count1 += 1

        # If counts of 0s and 1s are equal,
        # we found a balanced substring
        if count0 == count1:
            # Increment the balanced substring count
            maxCount += 1

    # Check if total number of 0s and 1s are equal
    if count0 != count1:
        # Not possible to split the string into balanced substrings
        return -1

    # Return the maximum count of balanced substrings
    return maxCount


# Example inputs
str1 = "0100110101"
str2 = "0111100010"
str3 = "0000000000"

print("Input:", str1, "-> Output:", maxBalancedSubstrings(str1))
print("Input:", str2, "-> Output:", maxBalancedSubstrings(str2))
print("Input:", str3, "-> Output:", maxBalancedSubstrings(str3))


'''
Time Complexity:
O(n)

Reason:

We traverse the binary string exactly once.

For every character, we only update count0 or count1
and compare the two counts.

Therefore:
O(n)


Space Complexity:
O(1)

Reason:

We only use three variables:

count0
count1
maxCount

No extra data structure is used.

Therefore:
O(1)
'''
