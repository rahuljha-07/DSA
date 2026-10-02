def findLargestSquare(i, j, mat, dp):
    n = len(mat)
    m = len(mat[0])
    if i >= n or j >= m:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if mat[i][j] == 0:
        dp[i][j] = 0
        return 0
    right = findLargestSquare(i, j + 1, mat, dp)
    down = findLargestSquare(i + 1, j, mat, dp)
    diagonal = findLargestSquare(i + 1, j + 1, mat, dp)
    dp[i][j] = 1 + min(right, down, diagonal)
    return dp[i][j]


def largestSquare(mat):
    n = len(mat)
    if n == 0 or not mat[0]:
        return 0
    m = len(mat[0])
    maxSize = 0
    dp = [[-1] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                maxSize = max(maxSize, findLargestSquare(i, j, mat, dp))
    return maxSize


def largestSquareBottomUp(mat):
    n = len(mat)
    if n == 0 or not mat[0]:
        return 0
    m = len(mat[0])
    maxSize = 0
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        dp[i][m - 1] = mat[i][m - 1]
        maxSize = max(maxSize, dp[i][m - 1])
    for j in range(m):
        dp[n - 1][j] = mat[n - 1][j]
        maxSize = max(maxSize, dp[n - 1][j])
    for i in range(n - 2, -1, -1):
        for j in range(m - 2, -1, -1):
            if mat[i][j] == 1:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
            else:
                dp[i][j] = 0
            maxSize = max(maxSize, dp[i][j])
    return maxSize


def main():
    mat1 = [[0, 1, 1, 0, 1], [1, 1, 0, 1, 0], [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
    mat2 = [[1, 1], [1, 1]]
    mat3 = [[0, 0], [0, 0]]
    for mat in (mat1, mat2, mat3):
        print("Largest square size:", largestSquare(mat))


if __name__ == "__main__":
    main()


'''
Let n/m be binary matrix rows/columns.
Time: O(n*m) for both methods: each cell stores the largest all-one
square starting there, using three neighbors in O(1) work.
Space: O(n*m) table; memoized largestSquare adds O(n+m) stack depth
because each recursive move increases row or column.
largestSquareBottomUp preserves the duplicate iterative implementation.
The returned value is side length, not square area.
'''
