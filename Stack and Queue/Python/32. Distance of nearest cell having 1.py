from collections import deque


def nearest(grid):
    # Find each cell's shortest distance to any cell containing 1.
    n = len(grid)  # Number of rows.
    m = len(grid[0])  # Number of columns.

    # A large value marks cells whose distance has not been found yet.
    # Python integers do not overflow, so C++'s INT_MAX-1 safeguard is unnecessary.
    v = [[10**18 for j in range(m)] for i in range(n)]
    q = deque()

    # Start BFS from all 1-cells together, not a separate BFS for each cell.
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                q.append((i, j))
                v[i][j] = 0  # A 1-cell is zero steps from itself.

    # Row/column changes for up, down, right, and left.
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    # FIFO processing explores cells in increasing distance from the nearest 1.
    while len(q) != 0:
        x = q[0][0]
        y = q[0][1]
        q.popleft()

        # Try all four neighbors of the current cell.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # Ignore positions outside the grid.
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                # Reaching this neighbor takes one more step than reaching (x, y).
                # Update and enqueue it only if this route improves its distance.
                if v[nx][ny] > v[x][y] + 1:
                    v[nx][ny] = v[x][y] + 1
                    q.append((nx, ny))

    # If the grid has no 1, every distance remains at the initial large value.
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
