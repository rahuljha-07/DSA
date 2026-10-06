def LCS(str1, str2):
    n = len(str1)
    m = len(str2)
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


def minInsertionsToMakePalindrome(str):
    # Reverse the input string
    rev = str[::-1]
    lenStr = len(str)

    # Call the LCS function (assumed to be defined elsewhere)
    # calling the LPS actually in LPS we reverse the 2nd string and everything is same as
    # LCS
    lcsLength = LCS(str, rev)

    # Calculate the number of insertions needed
    numInsertions = lenStr - lcsLength

    return numInsertions


str = "abcda"
print(minInsertionsToMakePalindrome(str))


'''
Time Complexity: O(n^2), where n is the string length.

Reason:
The string is reversed, then LCS is calculated between the original
string and the reversed string.
The LCS DP table has n rows and n columns.
Each cell is filled once with constant work.

Space Complexity: O(n^2)

Reason:
The DP table stores one value for every pair of indexes from the
original and reversed strings.
'''
