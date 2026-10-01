def maxDiff(matrix, n):
    # Create a 2D list to store the maximum values
    # seen from each position toward bottom-right
    maxMat = [[0 for _ in range(n)] for _ in range(n)]

    # Initialize bottom-right element
    maxMat[n - 1][n - 1] = matrix[n - 1][n - 1]

    # Fill the last row
    for j in range(n - 2, -1, -1):
        maxMat[n - 1][j] = max(
            matrix[n - 1][j],
            maxMat[n - 1][j + 1]
        )

    # Fill the last column
    for i in range(n - 2, -1, -1):
        maxMat[i][n - 1] = max(
            matrix[i][n - 1],
            maxMat[i + 1][n - 1]
        )

    # Fill the rest of maxMat
    for i in range(n - 2, -1, -1):
        for j in range(n - 2, -1, -1):

            maxMat[i][j] = max(
                maxMat[i + 1][j],
                maxMat[i][j + 1],
                matrix[i][j]
            )

    # Find maximum difference
    ans = float('-inf')

    for a in range(n - 1):
        for b in range(n - 1):

            ans = max(
                ans,
                maxMat[a + 1][b + 1] - matrix[a][b]
            )

    return ans


def solve():
    n = int(input())

    matrix = []

    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    print("MAX VALUE IS:", maxDiff(matrix, n))


tc = 1

while tc > 0:
    solve()
    tc -= 1


'''
Time Complexity:
O(n^2)

Reason:

1. Filling the last row takes:
O(n)

2. Filling the last column takes:
O(n)

3. Filling the remaining maxMat takes:
O(n^2)

4. Finding the maximum difference also takes:
O(n^2)

Therefore, overall time complexity is:

O(n^2)


Space Complexity:
O(n^2)

Reason:

We create an additional 2D matrix called maxMat
of size n x n.

Therefore:

O(n^2)
'''