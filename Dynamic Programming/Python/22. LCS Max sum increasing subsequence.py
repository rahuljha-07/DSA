def maxSumIncreasingSubsequence(arr):
    n = len(arr)
    sortedArr = list(arr)
    sortedArr.sort()
    sortedArr = list(dict.fromkeys(sortedArr))
    m = len(sortedArr)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr[i - 1] == sortedArr[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + arr[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]


def main():
    arr1 = [1, 101, 2, 3, 100]
    print("Maximum sum of increasing subsequence:", maxSumIncreasingSubsequence(arr1))
    arr2 = [4, 1, 2, 3]
    print("Maximum sum of increasing subsequence:", maxSumIncreasingSubsequence(arr2))
    arr3 = [4, 1, 2, 4]
    print("Maximum sum of increasing subsequence:", maxSumIncreasingSubsequence(arr3))


if __name__ == "__main__":
    main()


'''
Let n be elements and m<=n distinct values.
Time: O(n log(n+1)+(n+1)*(m+1)): sort a copy and fill the weighted
LCS table in constant work per state. Worst case is O((n+1)^2).
Space: O(n+(n+1)*(m+1)) auxiliary for sortedArr and the full table.
The source recurrence is retained; its match branch assumes positive
values. It is not a general signed-input maximum-sum solver.
'''
