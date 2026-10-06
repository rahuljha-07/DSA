from collections import deque


# Function to check adjacent cells and rot the fresh oranges
def issafe(grid, q, p):
    # Number of rows in the grid
    n = len(grid)
    # Number of columns in the grid
    m = len(grid[0])
    # Current row index
    x = p[0]
    # Current column index
    y = p[1]

    # Directions for adjacent cells: up, down, left, right
    v = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Check each direction
    for temp in v:
        # Calculate the new position
        newX = x + temp[0]
        newY = y + temp[1]

        # Check if the new position is within the grid boundaries
        if newX >= 0 and newX < n and newY >= 0 and newY < m:
            # If the adjacent cell is empty (0) or already rotten (2), continue to the next
            # direction
            if grid[newX][newY] == 0 or grid[newX][newY] == 2:
                continue
            else:
                # Push the position of the fresh orange (1) into the queue
                q.append((newX, newY))
                # Mark this orange as rotten (2)
                grid[newX][newY] = 2


def orangesRotting(grid):
    # Timer to count the minutes taken for all oranges to rot
    timer = 0
    # Count of rotten oranges at the current level
    count = 0
    q = deque()

    # Initialize the queue with positions of all rotten oranges
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # If the orange is rotten
            if grid[i][j] == 2:
                # Push its position into the queue
                q.append((i, j))

    # Count of rotten oranges in the queue
    count = len(q)

    # Process the queue until it is empty
    while len(q) != 0:
        # Process all oranges at the current level (current time step)
        for i in range(count):
            # Get the position of the current rotten orange
            p = q[0]
            # Remove the processed orange from the queue
            q.popleft()
            # Check and rot adjacent fresh oranges
            issafe(grid, q, p)

        # If there are any newly rotten oranges in the queue
        if len(q) > 0:
            # Update the count to the number of newly rotten oranges
            count = len(q)
            # Increment the timer as one minute has passed
            timer += 1

    # After processing, check if there are any fresh oranges left
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # If there is a fresh orange left, return -1
            if grid[i][j] == 1:
                return -1

    # Return the total time taken for all oranges to rot
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
