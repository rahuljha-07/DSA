def maxLengthEqual01(nums):
    prefixSumMap = {0: -1}
    prefixSum = 0
    maxLength = 0
    for i in range(len(nums)):
        # Transform 0 to -1 to balance with 1s
        prefixSum += -1 if nums[i] == 0 else 1
        if prefixSum in prefixSumMap:
            # Calculate the length of the balanced subarray
            maxLength = max(maxLength, i - prefixSumMap[prefixSum])
        else:
            # Store the first occurrence of the prefix sum
            prefixSumMap[prefixSum] = i
    return maxLength


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
    # Number of rows
    n = len(matrix)
    # Number of columns
    m = len(matrix[0])
    maxArea = 0
    # Initialize column sums to 0
    columnSums = [0] * m
    # Extend the submatrix downwards from rowStart
    for rowEnd in range(rowStart, n):
        for col in range(m):
            columnSums[col] += -1 if matrix[rowEnd][col] == 0 else 1
        # Calculate the maximum zero-sum subarray length in the current column sums
        maxWidth = maxZeroSumSubarray(columnSums)
        # Calculate the area of the current submatrix
        height = rowEnd - rowStart + 1
        currentArea = maxWidth * height
        # Update the maximum area found
        maxArea = max(maxArea, currentArea)
    return maxArea


def largestSubmatrixWithEqual01(matrix):
    n = len(matrix)
    if n == 0 or not matrix[0]:
        return 0
    maxArea = 0
    # Iterate over each starting row
    for rowStart in range(n):
        # Call the solve function for each rowStart
        maxArea = max(maxArea, solve(matrix, rowStart))
    return maxArea


def main():
    matrix = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 1, 0], [1, 0, 0, 1]]
    print("Largest Submatrix with Equal 0's and 1's Area:",
          largestSubmatrixWithEqual01(matrix), "sq. units")


if __name__ == "__main__":
    main()


'''
Let n/m be binary matrix rows/columns.
Time: O(n^2*m) expected: for every row pair, add -1 for zeros and +1
for ones to m column sums, then find a longest zero-sum column interval
in O(m) with expected O(1) hash operations. Zero sum means equal counts.
Space: O(m) auxiliary column sums and prefix map; no converted matrix
is allocated. maxLengthEqual01 is the retained 1D helper with O(m) time/
space on m values. The 2D function returns area and leaves input unchanged.
'''
