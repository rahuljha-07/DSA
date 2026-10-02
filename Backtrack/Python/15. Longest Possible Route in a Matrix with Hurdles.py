rowDir = [-1, 1, 0, 0]
colDir = [0, 0, -1, 1]


def isSafe(x, y, matrix, visited):
    rows = len(matrix)
    cols = len(matrix[0])
    return 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 1 and not visited[x][y]


def findLongestPath(matrix, visited, srcX, srcY, destX, destY, pathLen, maxPathLen):
    if srcX == destX and srcY == destY:
        maxPathLen[0] = max(maxPathLen[0], pathLen)
        return
    visited[srcX][srcY] = True
    for i in range(4):
        newX = srcX + rowDir[i]
        newY = srcY + colDir[i]
        if isSafe(newX, newY, matrix, visited):
            findLongestPath(matrix, visited, newX, newY, destX, destY,
                            pathLen + 1, maxPathLen)
    visited[srcX][srcY] = False


def main():
    matrix = [[1,1,1,1,1,1,1,1], [1,0,0,1,0,0,0,1],
              [1,1,1,1,1,1,0,1], [0,0,0,0,1,0,0,1], [1,1,1,1,1,1,1,1]]
    srcX = 0
    srcY = 0
    destX = 4
    destY = 7
    if matrix[srcX][srcY] == 0 or matrix[destX][destY] == 0:
        print("No path possible")
        return
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    maxPathLen = [-1]
    findLongestPath(matrix, visited, srcX, srcY, destX, destY, 0, maxPathLen)
    print(f"Longest Path Length: {maxPathLen[0]}" if maxPathLen[0] >= 0
          else "No path possible")


if __name__ == "__main__":
    main()


'''
Let A=rows*cols be matrix cells.
Time: O(4^A) conservative upper bound: enumerate simple paths with up
to four neighbors per recursive level, to depth at most A.
Space: O(A) auxiliary visited grid and recursive depth; matrix is unchanged.
Length counts edges. A -1 initial best distinguishes no path from a valid
zero-edge source==destination path; endpoints must be safe and in bounds.
'''
