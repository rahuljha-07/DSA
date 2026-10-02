t = []


def LCS(n, m, str1, str2):
    if n == 0 or m == 0:
        return 0

    if t[n][m] != -1:
        return t[n][m]

    if str1[n - 1] == str2[m - 1]:
        t[n][m] = 1 + LCS(n - 1, m - 1, str1, str2)
    else:
        t[n][m] = max(LCS(n - 1, m, str1, str2), LCS(n, m - 1, str1, str2))

    return t[n][m]


def lcs(n, m, str1, str2):
    global t
    t = [[-1 for j in range(m + 1)] for i in range(n + 1)]
    return LCS(n, m, str1, str2)


def lcsTopDown(n, m, str1, str2):
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

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
