INT_MIN = float("-inf")


def maxPathSumHelper(mat, r, c, n, dp):
    if c < 0 or c >= len(mat[0]):
        return INT_MIN
    if r == n - 1:
        return mat[r][c]
    if dp[r][c] is not None:
        return dp[r][c]
    down = maxPathSumHelper(mat, r + 1, c, n, dp)
    downLeft = maxPathSumHelper(mat, r + 1, c - 1, n, dp)
    downRight = maxPathSumHelper(mat, r + 1, c + 1, n, dp)
    dp[r][c] = mat[r][c] + max(down, downLeft, downRight)
    return dp[r][c]


def maxPathSum(mat):
    n = len(mat)
    if n == 0 or not mat[0]:
        return 0
    m = len(mat[0])
    maxSum = INT_MIN
    dp = [[None] * m for _ in range(n)]
    for c in range(m):
        maxSum = max(maxSum, maxPathSumHelper(mat, 0, c, n, dp))
    return maxSum


def maxPathSumBottomUp(mat):
    n = len(mat)
    if n == 0 or not mat[0]:
        return 0
    m = len(mat[0])
    dp = [row[:] for row in mat]
    for row in range(n - 2, -1, -1):
        for col in range(m):
            down = dp[row + 1][col]
            downLeft = dp[row + 1][col - 1] if col > 0 else INT_MIN
            downRight = dp[row + 1][col + 1] if col < m - 1 else INT_MIN
            dp[row][col] += max(down, downLeft, downRight)
    return max(dp[0])


def main():
    mat1 = [[348, 391], [618, 193]]
    mat2 = [[2, 2], [2, 2]]
    mat3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat4 = [[10, 10, 2, 0, 20, 4], [1, 0, 0, 30, 2, 5],
            [0, 10, 4, 0, 2, 0], [1, 0, 2, 20, 0, 4]]
    for mat in (mat1, mat2, mat3, mat4):
        print("Maximum path sum:", maxPathSum(mat))


if __name__ == "__main__":
    main()


'''
Let n/m be matrix rows/columns.
Time: O(n*m) for either method: each cell combines three downward
neighbors once. Top-down uses None so a valid -1 sum remains cached.
Space: O(n*m) auxiliary table/copy; top-down also adds O(n) stack depth.
Rows are copied separately in bottom-up, leaving mat unchanged.
The source's square-only indexing is corrected for its rectangular demo;
the same downward/down-diagonal recurrence is preserved.
'''
