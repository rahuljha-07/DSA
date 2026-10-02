def editDistanceMemoHelper(s1, s2, i, j, dp):
    if i == len(s1):
        return len(s2) - j
    if j == len(s2):
        return len(s1) - i
    if dp[i][j] != -1:
        return dp[i][j]
    if s1[i] == s2[j]:
        dp[i][j] = editDistanceMemoHelper(s1, s2, i + 1, j + 1, dp)
        return dp[i][j]
    insertOp = 1 + editDistanceMemoHelper(s1, s2, i, j + 1, dp)
    removeOp = 1 + editDistanceMemoHelper(s1, s2, i + 1, j, dp)
    replaceOp = 1 + editDistanceMemoHelper(s1, s2, i + 1, j + 1, dp)
    dp[i][j] = min(insertOp, removeOp, replaceOp)
    return dp[i][j]


def editDistanceMemo(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[-1] * n for _ in range(m)]
    return editDistanceMemoHelper(s1, s2, 0, 0, dp)


def main():
    s1 = "geek"
    s2 = "gesek"
    print("Edit Distance (Memoization):", editDistanceMemo(s1, s2))


if __name__ == "__main__":
    main()


'''
Let m/n be string lengths.
Time: O(m*(n+1)+1): each suffix-index pair is memoized once with at most
three insertion/deletion/replacement transitions. Empty strings return
their required edits immediately, but allocating m empty rows still costs
O(m) when n=0. For nonempty strings this is the usual O(m*n).
Space: O(m*n+m+n) auxiliary: m rows of n memo cells plus a recursion
chain of at most m+n calls. Strings are passed without substring copying.
'''
