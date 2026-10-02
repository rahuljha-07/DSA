def subsetSumTopDownHelper(arr, n, sum, t):
    if sum == 0:
        return True
    if n == 0:
        return False
    if t[n][sum] != -1:
        return t[n][sum]
    if arr[n - 1] <= sum:
        t[n][sum] = (subsetSumTopDownHelper(arr, n - 1, sum - arr[n - 1], t)
                     or subsetSumTopDownHelper(arr, n - 1, sum, t))
    else:
        t[n][sum] = subsetSumTopDownHelper(arr, n - 1, sum, t)
    return t[n][sum]


def equalSumPartitionTopDown(arr, n):
    totalSum = 0
    for i in range(n):
        totalSum += arr[i]
    if totalSum % 2 != 0:
        return False
    targetSum = totalSum // 2
    t = [[-1] * (targetSum + 1) for _ in range(n + 1)]
    return subsetSumTopDownHelper(arr, n, targetSum, t)


def equalPartition(n, arr):
    sum = 0
    for i in range(n):
        sum += arr[i]
    if sum % 2 != 0 or sum == 0:
        return 0
    return int(subset(arr, n, sum // 2))


def subset(arr, n, sum):
    t = [[False] * (sum + 1) for _ in range(n + 1)]
    for i in range(sum + 1):
        t[0][i] = False
    for i in range(n + 1):
        t[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]
    return t[n][sum]


def main():
    arr = [1, 5, 11, 5]
    n = len(arr)
    print("The array can be partitioned into two subsets with equal sum."
          if equalSumPartitionTopDown(arr, n)
          else "The array cannot be partitioned into two subsets with equal sum.")


if __name__ == "__main__":
    main()


'''
Let n be element count and S half the total nonnegative sum.
Time: O(n) to total values, then O((n+1)*(S+1)) table allocation/state work.
An odd total returns after O(n), without a table.
Space: O((n+1)*(S+1)) auxiliary table; recursive method adds O(n) stack.
Both source variants are preserved: equalPartition explicitly rejects
zero total, while equalSumPartitionTopDown accepts zero/empty sums.
Values must be nonnegative; complexity is pseudo-polynomial in S.
'''
