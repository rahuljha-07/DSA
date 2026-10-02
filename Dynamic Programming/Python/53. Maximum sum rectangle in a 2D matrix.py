INT_MIN = float("-inf")


def maxSubarraySum(arr):
    maxi = INT_MIN
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        maxi = max(maxi, sum)
        if sum < 0:
            sum = 0
    return maxi


def solve(matrix, rowStart):
    n = len(matrix)
    m = len(matrix[0])
    maxSum = INT_MIN
    columnSums = [0] * m
    for rowEnd in range(rowStart, n):
        for col in range(m):
            columnSums[col] += matrix[rowEnd][col]
        bestHere = maxSubarraySum(columnSums)
        maxSum = max(maxSum, bestHere)
    return maxSum


def maximumSumRectangle(matrix):
    n = len(matrix)
    if n == 0 or not matrix[0]:
        return 0
    ans = INT_MIN
    for rowStart in range(n):
        ans = max(ans, solve(matrix, rowStart))
    return ans


def main():
    mat = [[1, 2, 1, 4, 20], [8, 3, 4, 2, 1],
           [3, 8, 10, 1, 3], [4, 1, 1, 7, 6]]
    print("Maximum Sum Rectangle:", maximumSumRectangle(mat))


if __name__ == "__main__":
    main()


'''
Let n/m be matrix rows/columns.
Time: O(n^2*m): choose all O(n^2) row pairs, updating m column sums
and running O(m) Kadane each time. No rectangle's cells are rescanned
individually after compression.
Space: O(m) auxiliary columnSums; Kadane itself uses O(1) extra space.
Updating maxi before resetting sum preserves the largest negative value
for all-negative input. The matrix is not modified; empty input returns 0.
'''
