# Function to build the prefix table (longest prefix suffix array) for the pattern
def buildPrefixTable(pattern):
    patternLength = len(pattern)
    prefixTable = [0] * patternLength
    # Length of previous longest prefix suffix
    j = 0

    # Build the prefix table
    for i in range(1, patternLength):
        while j > 0 and pattern[i] != pattern[j]:
            # Fallback in the prefix table
            j = prefixTable[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefixTable[i] = j
    return prefixTable


# KMP search function to find all occurrences of the pattern in the text
def kmpSearch(text, pattern):
    prefixTable = buildPrefixTable(pattern)
    # To store the starting indices of all matches
    matchIndices = []
    # Index for pattern
    j = 0

    # Traverse the text
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = prefixTable[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            # Match found; store index
            matchIndices.append(i - j + 1)
            # Reset j based on prefix table
            j = prefixTable[j - 1]
    return matchIndices


text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

result = kmpSearch(text, pattern)

print("Pattern found at indices:", end=" ")
for index in result:
    print(index, end=" ")
print()


'''
Time Complexity: O(n + m), where n is text length and m is pattern length.

Reason:
Building the prefix table takes O(m) because every pattern character
is processed once.

The text scan takes O(n). Even when j moves backward using the prefix
table, it never causes repeated full scans of the text.

Space Complexity: O(m)

Reason:
The prefix table stores one value for every character in the pattern.
Apart from that, only indexes and the output list are used.
'''
