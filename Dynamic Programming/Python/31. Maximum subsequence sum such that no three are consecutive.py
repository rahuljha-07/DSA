def maxSumNoThreeConsecutiveHelper(arr, n, dp):
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return arr[0] + arr[1]
    if dp[n] != -1:
        return dp[n]
    dp[n] = max(
        maxSumNoThreeConsecutiveHelper(arr, n - 1, dp),
        arr[n - 1] + maxSumNoThreeConsecutiveHelper(arr, n - 2, dp),
        arr[n - 1] + arr[n - 2] + maxSumNoThreeConsecutiveHelper(arr, n - 3, dp),
    )
    return dp[n]


def maxSumNoThreeConsecutive(arr):
    n = len(arr)
    dp = [-1] * (n + 1)
    return maxSumNoThreeConsecutiveHelper(arr, n, dp)


def main():
    arr1 = [1, 2, 3]
    arr2 = [3000, 2000, 1000, 3, 10]
    arr3 = [100, 1000, 100, 1000, 1]
    arr4 = [1, 1, 1, 1, 1]
    arr5 = [1, 2, 3, 4, 5, 6, 7, 8]
    for arr in (arr1, arr2, arr3, arr4, arr5):
        print("Maximum sum:", maxSumNoThreeConsecutive(arr))


if __name__ == "__main__":
    main()


'''
Let n be array length, assuming nonnegative values as in the source.
Time: O(n+1): each prefix length is memoized once, combining three
choices in O(1) work. Recursion does not enumerate all subsets.
Space: O(n+1) auxiliary memo array and O(n) deepest recursion chain.
The n=1/2 bases take all values; signed-input optimization is not added.
'''
