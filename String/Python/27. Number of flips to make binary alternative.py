def minFlipsToAlternating(s):
    # Flips needed for the pattern "010101..."
    countFlipsToPattern1 = 0
    # Flips needed for the pattern "101010..."
    countFlipsToPattern2 = 0

    for i in range(len(s)):
        # Checking for even index
        if i % 2 == 0:
            if s[i] == '1':
                # Pattern 1 needs to increment for '1' at even
                # Pattern 1 needs to increment for '0' at odd
                countFlipsToPattern1 += 1
            # i % 2 != 0, checking for odd index
            else:
                # Pattern 2 needs to increment for '0' at even
                # Pattern 2 needs to increment for '1' at odd
                countFlipsToPattern2 += 1
        else:
            if s[i] == '0':
                countFlipsToPattern1 += 1
            else:
                countFlipsToPattern2 += 1

    # Return the minimum flips required to convert to either pattern
    return min(countFlipsToPattern1, countFlipsToPattern2)


binaryString = "001"
result = minFlipsToAlternating(binaryString)
print("Minimum number of flips:", result)


'''
Time Complexity: O(n), where n is the string length.

Reason:
The string is scanned once.
At each index, we compare the current character with the two possible
alternating patterns and update counters.

Space Complexity: O(1)

Reason:
Only two counters and loop variables are used.
No extra structure depends on n.
'''
