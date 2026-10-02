from collections import deque


def nearest(grid):
    n = len(grid)
    m = len(grid[0])

    v = [[10**18 for j in range(m)] for i in range(n)]
    q = deque()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                q.append((i, j))
                v[i][j] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    while len(q) != 0:
        x = q[0][0]
        y = q[0][1]
        q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if v[nx][ny] > v[x][y] + 1:
                    v[nx][ny] = v[x][y] + 1
                    q.append((nx, ny))

    return v


grid = [
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 1]
]

result = nearest(grid)
for row in result:
    for distance in row:
        print(distance, end=" ")
    print()


'''
Time Complexity: O(n * m)

Reason:
Multi-source BFS starts from every cell containing 1. Each matrix cell can be
relaxed and pushed into the queue at most once with its shortest distance.

Space Complexity: O(n * m)

Reason:
The distance matrix and BFS queue can both store up to n * m cells.
'''
