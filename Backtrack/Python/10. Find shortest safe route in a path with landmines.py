import sys


def findShortestSafeRoute(rows, cols, unsafeCells, visited, currentRow, currentCol, steps):
    if (currentRow < 0 or currentRow >= rows or currentCol < 0 or currentCol >= cols
            or (currentRow, currentCol) in unsafeCells or visited[currentRow][currentCol]):
        return float("inf")
    if currentCol == cols - 1:
        return steps
    visited[currentRow][currentCol] = True
    moveDown = findShortestSafeRoute(rows, cols, unsafeCells, visited, currentRow + 1, currentCol, steps + 1)
    moveUp = findShortestSafeRoute(rows, cols, unsafeCells, visited, currentRow - 1, currentCol, steps + 1)
    moveRight = findShortestSafeRoute(rows, cols, unsafeCells, visited, currentRow, currentCol + 1, steps + 1)
    moveLeft = findShortestSafeRoute(rows, cols, unsafeCells, visited, currentRow, currentCol - 1, steps + 1)
    visited[currentRow][currentCol] = False
    return min(moveDown, moveUp, moveRight, moveLeft)


def shortestPath(grid, rows, cols):
    if rows == 0 or cols == 0:
        return -1
    unsafeCells = set()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                unsafeCells.add((i, j))
                if i + 1 < rows:
                    unsafeCells.add((i + 1, j))
                if i - 1 >= 0:
                    unsafeCells.add((i - 1, j))
                if j + 1 < cols:
                    unsafeCells.add((i, j + 1))
                if j - 1 >= 0:
                    unsafeCells.add((i, j - 1))
    visited = [[False] * cols for _ in range(rows)]
    shortestRoute = float("inf")
    for i in range(rows):
        if (i, 0) not in unsafeCells:
            pathLength = findShortestSafeRoute(rows, cols, unsafeCells, visited, i, 0, 0)
            shortestRoute = min(shortestRoute, pathLength)
    return -1 if shortestRoute == float("inf") else shortestRoute


def main():
    tokens = iter(sys.stdin.read().split())
    print("Enter the number of rows and columns: ", end="")
    rows = int(next(tokens))
    cols = int(next(tokens))
    print("Enter the grid (0 for landmine, 1 for safe cell):")
    grid = [[int(next(tokens)) for _ in range(cols)] for _ in range(rows)]
    result = shortestPath(grid, rows, cols)
    print("No safe route exists." if result == -1
          else f"The length of the shortest safe route is: {result}")


if __name__ == "__main__":
    main()


'''
Let A=rows*cols be cells.
Time: O(A + rows*4^A) conservative worst-case bound: mark mines/neighbors,
then backtrack simple paths from each first-column seed with up to four
moves per depth A. The retained approach is exhaustive DFS, not shortest-
path BFS, and revisits cells on different paths.
Space: O(A) auxiliary unsafe-cell hash set, visited grid, and recursive
depth. Hash membership averages O(1); supplied grid is not changed.
'''
