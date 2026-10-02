def subsetHelper(dp, arr, n, sum):
    if sum == 0:
        return True
    if n == 0:
        return False
    if dp[n][sum] != -1:
        return dp[n][sum]
    if arr[n - 1] <= sum:
        dp[n][sum] = (subsetHelper(dp, arr, n - 1, sum - arr[n - 1])
                      or subsetHelper(dp, arr, n - 1, sum))
    else:
        dp[n][sum] = subsetHelper(dp, arr, n - 1, sum)
    return dp[n][sum]


def subsetSumPartition(n, arr, sum):
    dp = [[-1] * (sum + 1) for _ in range(n + 1)]
    return subsetHelper(dp, arr, n, sum)


def subsetSumTopDown(arr, n, sum):
    t = [[False] * (sum + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        t[i][0] = True
    for j in range(1, sum + 1):
        t[0][j] = False
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]
    return t[n][sum]


def main():
    arr = [2, 3, 7, 8, 10]
    n = len(arr)
    sum = 11
    print("Subset with the given sum exists." if subsetSumPartition(n, arr, sum)
          else "Subset with the given sum does not exist.")


if __name__ == "__main__":
    main()


'''
Let n be element count and S the nonnegative target sum.
Time: O((n+1)*(S+1)) for both: allocate the full table, then compute at
most one constant-time result per (item count, remaining sum) state.
Space: O((n+1)*(S+1)) auxiliary table; memoized recursion adds O(n) stack.
Despite its source name, subsetSumTopDown is bottom-up tabulation.
These are pseudo-polynomial bounds; array values must be nonnegative.
'''
