def longestSubsequence(n, a):
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if abs(a[i] - a[j]) == 1:
                dp[i] = max(dp[i], dp[j] + 1)
    ma = 0
    for i in range(n):
        ma = max(ma, dp[i])
    return ma


def main():
    n = 7
    a = [1, 2, 3, 4, 5, 3, 2]
    print("Length of the longest subsequence:", longestSubsequence(n, a))


if __name__ == "__main__":
    main()


'''
Let n be array length.
Time: O(n^2): for each ending index i, all i earlier indices are checked;
the checks total 0+1+...+(n-1). Initialization/final maximum add O(n).
Space: O(n) auxiliary dp, storing the best length ending at each index.
Adjacent refers to consecutive chosen subsequence elements, not array indices.
'''
