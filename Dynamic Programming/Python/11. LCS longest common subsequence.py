t = []


def LCS(x, y, n, m):
    if n == 0 or m == 0:
        return 0
    if t[n][m] != -1:
        return t[n][m]
    if x[n - 1] == y[m - 1]:
        t[n][m] = 1 + LCS(x, y, n - 1, m - 1)
    else:
        t[n][m] = max(LCS(x, y, n - 1, m), LCS(x, y, n, m - 1))
    return t[n][m]


def computeLCS(x, y):
    n = len(x)
    m = len(y)
    t[:] = [[-1] * (m + 1) for _ in range(n + 1)]
    return LCS(x, y, n, m)


def LCSBottomUp(x, y):
    n = len(x)
    m = len(y)
    t = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])
    return t[n][m]


def main():
    x = "AGGTAB"
    y = "GXTXAYB"
    print("Length of LCS:", computeLCS(x, y))


if __name__ == "__main__":
    main()


'''
Let n/m be the two sequence lengths.
Time: O((n+1)*(m+1)): each prefix pair is a DP state with one character
comparison and at most two neighboring table lookups.
Space: O((n+1)*(m+1)) for the full 2D table; no row compression is used.
Memoized LCS also needs O(n+m) recursive stack; computeLCS resets t.
The iterative overload is exposed as LCSBottomUp.
'''
