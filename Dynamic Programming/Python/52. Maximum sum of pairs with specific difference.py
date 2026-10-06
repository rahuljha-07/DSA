def maxSumOfPairsWithDiffLessThanK(a, K):
    a = list(a)
    a.sort()
    ans = 0
    i = len(a) - 1
    while i > 0:
        if a[i] - a[i - 1] < K:
            ans += a[i] + a[i - 1]
            # use both
            # skip the larger one
            i -= 2
        else:
            i -= 1
    return ans


def main():
    arr1 = [3, 5, 10, 15, 17, 12, 9]
    K1 = 4
    print(maxSumOfPairsWithDiffLessThanK(arr1, K1))
    arr2 = [5, 15, 10, 300]
    K2 = 12
    print(maxSumOfPairsWithDiffLessThanK(arr2, K2))


if __name__ == "__main__":
    main()


'''
Let n be array length, assuming nonnegative values.
Time: O(n log(n+1)): sorting dominates the backward scan, where i
decreases by one or two each iteration. Difference must be strictly <K.
Space: O(n) auxiliary for a copy and Python sort workspace. The copy
preserves C++'s pass-by-value behavior, leaving the caller's array unchanged.
The source takes every eligible pair; signed-input pair skipping is not added.
'''
