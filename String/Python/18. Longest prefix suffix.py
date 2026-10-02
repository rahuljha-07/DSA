def buildPrefixTable(str):
    n = len(str)
    prefixTable = [0] * n
    j = 0

    for i in range(1, n):
        while j > 0 and str[i] != str[j]:
            j = prefixTable[j - 1]
        if str[i] == str[j]:
            j += 1
        prefixTable[i] = j

    return prefixTable


def longestPrefixSuffix(str):
    prefixTable = buildPrefixTable(str)

    maxLPS = 0
    for i in range(len(prefixTable)):
        maxLPS = max(maxLPS, prefixTable[i])

    return maxLPS


str1 = "abab"
str2 = "aaaa"
str3 = "abcdabc"
str4 = "abcab"

print("Longest Prefix Suffix length for '" + str1 + "':", longestPrefixSuffix(str1))
print("Longest Prefix Suffix length for '" + str2 + "':", longestPrefixSuffix(str2))
print("Longest Prefix Suffix length for '" + str3 + "':", longestPrefixSuffix(str3))
print("Longest Prefix Suffix length for '" + str4 + "':", longestPrefixSuffix(str4))


'''
Time Complexity: O(n), where n is the string length.

Reason:
The prefix table loop goes through the string once.
When j moves backward, it uses previously computed prefix values,
so characters are not repeatedly rescanned from the beginning.

Finding maxLPS also scans the prefix table once.
So total work is O(n).

Space Complexity: O(n)

Reason:
The prefixTable list stores one integer for each character of the string.
'''
