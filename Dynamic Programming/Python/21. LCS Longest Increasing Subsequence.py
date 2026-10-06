# Function to compute LCS of two arrays
def LCS(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    # Create a DP table
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr1[i - 1] == arr2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # The length of LCS
    return dp[n][m]


# Function to find the length of the longest increasing subsequence
def longestSubsequence(arr):
    sortedArr = list(arr)
    # Sort and remove duplicates
    sortedArr.sort()
    sortedArr = list(dict.fromkeys(sortedArr))
    # Find the LCS between arr and sortedArr
    return LCS(arr, sortedArr)


'''
Let n be array length and m<=n the number of distinct values.
Time: O(n log(n+1)+(n+1)*(m+1)): sort/deduplicate a copy, then fill
an n-by-m LCS table against the sorted unique values.
Space: O(n+(n+1)*(m+1)) auxiliary for sortedArr, deduplication/sorting
workspace, and DP. Worst-case time and space are O((n+1)^2).
Removing duplicates makes the increasing subsequence STRICT, as in C++.
'''
