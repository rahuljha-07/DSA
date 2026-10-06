t = []


def LCS(n, m, str1, str2):
    # Base case: if either string is empty, the LCS is 0
    if n == 0 or m == 0:
        return 0

    # Check if the result is already calculated
    if t[n][m] != -1:
        return t[n][m]

    # If the last characters match, add 1 to the result and move both indices
    if str1[n - 1] == str2[m - 1]:
        t[n][m] = 1 + LCS(n - 1, m - 1, str1, str2)
    else:
        # If last characters don't match, take the max by either moving `n` or `m`
        t[n][m] = max(LCS(n - 1, m, str1, str2), LCS(n, m - 1, str1, str2))

    return t[n][m]


def lcs(n, m, str1, str2):
    global t
    # Initialize the memoization table with -1
    t = [[-1 for j in range(m + 1)] for i in range(n + 1)]
    # Call the helper LCS function
    return LCS(n, m, str1, str2)


# top down approach
def lcsTopDown(n, m, str1, str2):
    # Create a 2D DP table initialized with 0
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

    # Build the DP table iteratively
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If characters match, add 1 to the result from previous indices
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                # If characters don't match, take the maximum LCS by moving one index in
                # either string
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The LCS length will be in the bottom-right cell of the DP table
    return dp[n][m]


str1 = "AGGTAB"
str2 = "GXTXAYB"
print(lcs(len(str1), len(str2), str1, str2))
print(lcsTopDown(len(str1), len(str2), str1, str2))


'''
Time Complexity: O(n * m), where n and m are string lengths.

Reason:
Each state represents one pair of lengths: n from str1 and m from str2.
So there are n * m possible states.

In memoization, each state is solved once and then reused.
In the top-down DP table, each cell is also filled once.
Each state/cell does constant work after checking characters.

Space Complexity: O(n * m)

Reason:
The memoization table or DP table stores one value for every pair
of indexes from the two strings.
The recursive version also uses stack space, but the table is the
dominant space usage.
'''
