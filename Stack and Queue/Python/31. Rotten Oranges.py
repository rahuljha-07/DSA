from collections import deque


def issafe(grid, q, p):
    n = len(grid)
    m = len(grid[0])
    x = p[0]
    y = p[1]

    v = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for temp in v:
        newX = x + temp[0]
        newY = y + temp[1]

        if newX >= 0 and newX < n and newY >= 0 and newY < m:
            if grid[newX][newY] == 0 or grid[newX][newY] == 2:
                continue
            else:
                q.append((newX, newY))
                grid[newX][newY] = 2


def orangesRotting(grid):
    timer = 0
    count = 0
    q = deque()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                q.append((i, j))

    count = len(q)

    while len(q) != 0:
        for i in range(count):
            p = q[0]
            q.popleft()
            issafe(grid, q, p)

        if len(q) > 0:
            count = len(q)
            timer += 1

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                return -1

    return timer


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
result = orangesRotting(grid)
print("Time taken for all oranges to rot:", result, "minutes.")


'''
Time Complexity: O(n * m)

Reason:
Each cell is enqueued and processed at most once during BFS, then the grid is
scanned once more to check for remaining fresh oranges.

Space Complexity: O(n * m)

Reason:
The queue can store many grid cells in the worst case.
'''
