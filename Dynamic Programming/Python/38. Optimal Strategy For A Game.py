def solve(i, j, a, dp):
    if i > j:
        return 0
    if i == j:
        return a[i]
    if dp[i][j] is not None:
        return dp[i][j]
    take_first = a[i] + min(solve(i + 2, j, a, dp), solve(i + 1, j - 1, a, dp))
    take_last = a[j] + min(solve(i + 1, j - 1, a, dp), solve(i, j - 2, a, dp))
    dp[i][j] = max(take_first, take_last)
    return dp[i][j]


def maxAmount(n, a):
    dp = [[None] * n for _ in range(n)]
    return solve(0, n - 1, a, dp)


def main():
    arr = [8, 15, 3, 7]
    n = len(arr)
    print("Maximum amount that can be won:", maxAmount(n, arr))


if __name__ == "__main__":
    main()


'''
Let n be the coin count.
Time: O(n^2): at most n*n interval states, each with a constant number
of endpoint choices/opponent responses. Memoization avoids repeated games.
Space: O(n^2) memo table plus O(n) recursive depth.
The missing i>j base case is added so even-length games terminate safely.
None distinguishes uncomputed states from valid negative winnings.
'''
