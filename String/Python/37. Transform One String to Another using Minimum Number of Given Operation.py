memo = []


def LCS(n, m, str1, str2):
    if n == 0 or m == 0:
        return 0

    if memo[n][m] != -1:
        return memo[n][m]

    if str1[n - 1] == str2[m - 1]:
        memo[n][m] = 1 + LCS(n - 1, m - 1, str1, str2)
    else:
        memo[n][m] = max(LCS(n - 1, m, str1, str2), LCS(n, m - 1, str1, str2))

    return memo[n][m]


def lcs(n, m, str1, str2):
    global memo
    memo = [[-1 for j in range(m + 1)] for i in range(n + 1)]
    return LCS(n, m, str1, str2)


def transform(A, B):
    lcsLength = lcs(len(A), len(B), A, B)

    numDeletions = len(A) - lcsLength
    numInsertions = len(B) - lcsLength

    return numInsertions + numDeletions


A = "heap"
B = "pea"
print(transform(A, B))


'''
Time Complexity: O(n * m), where n and m are lengths of A and B.

Reason:
The transformation is based on LCS.
The LCS recursion has states based on indexes from A and B.
There are n * m such states, and memoization computes each one once.

Space Complexity: O(n * m)

Reason:
The memo table stores one answer for each pair of indexes.
The recursion stack is smaller than the table and does not dominate.
'''
