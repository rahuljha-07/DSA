def maxZeroSumSubarray(columnSums):
    prefixSumMap = {0: -1}
    prefixSum = 0
    maxLength = 0
    for col in range(len(columnSums)):
        prefixSum += columnSums[col]
        if prefixSum in prefixSumMap:
            length = col - prefixSumMap[prefixSum]
            maxLength = max(maxLength, length)
        else:
            prefixSumMap[prefixSum] = col
    return maxLength


def solve(matrix, rowStart):
    n = len(matrix)
    m = len(matrix[0])
    maxArea = 0
    columnSums = [0] * m
    for rowEnd in range(rowStart, n):
        for col in range(m):
            columnSums[col] += matrix[rowEnd][col]
        maxWidth = maxZeroSumSubarray(columnSums)
        height = rowEnd - rowStart + 1
        currentArea = maxWidth * height
        maxArea = max(maxArea, currentArea)
    return maxArea


def largestSubmatrixWithSumZero(matrix):
    n = len(matrix)
    if n == 0 or not matrix[0]:
        return 0
    maxArea = 0
    for rowStart in range(n):
        maxArea = max(maxArea, solve(matrix, rowStart))
    return maxArea


def main():
    matrix = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 1, 0], [1, 0, 0, 1]]
    print("Largest Submatrix with Sum 0 Area:", largestSubmatrixWithSumZero(matrix))


if __name__ == "__main__":
    main()


'''
Let n/m be rows/columns.
Time: O(n^2*m) expected: choose n*(n+1)/2 row-start/end pairs, update
m column sums, and scan those m sums with a prefix hash map. Equal
prefix sums delimit a zero-sum interval; keeping first occurrences gives
the widest interval. Hash-map operations are expected O(1).
Space: O(m) auxiliary columnSums and prefixSumMap, reused per row pair.
The input matrix is unchanged; the function returns area, not cells.
'''
