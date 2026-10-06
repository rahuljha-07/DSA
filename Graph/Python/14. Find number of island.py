directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (-1, 1), (1, -1), (1, 1)]


# Helper function to perform DFS
def dfs(row, col, grid, visited):
    n = len(grid)
    m = len(grid[0])
    visited[row][col] = True
    # Explore all 8 possible directions
    for dir in directions:
        newRow = row + dir[0]
        newCol = col + dir[1]
        if (0 <= newRow < n and 0 <= newCol < m
                and grid[newRow][newCol] == '1' and not visited[newRow][newCol]):
            dfs(newRow, newCol, grid, visited)


# Function to count the number of islands
def numIslands(grid):
    if not grid or not grid[0]:
        return 0
    n = len(grid)
    m = len(grid[0])
    # Visited array
    visited = [[False] * m for _ in range(n)]
    count = 0
    # Traverse the entire grid
    for i in range(n):
        for j in range(m):
            # If it's land ('1') and not visited, it's a new island
            if grid[i][j] == '1' and not visited[i][j]:
                # Increment the island count
                count += 1
                # Perform DFS to mark the whole island
                dfs(i, j, grid, visited)
    return count


def main():
    grid = [list("11000"), list("11000"), list("00100"), list("00011")]
    print("Number of Islands:", numIslands(grid))


if __name__ == "__main__":
    main()


'''
Let R/C be grid dimensions.
Time: O(R*C): scan every cell; each land cell is DFS-visited once and
checks eight constant-direction neighbors.
Space: O(R*C) auxiliary visited grid and worst-case recursive stack.
Eight-way connectivity (including diagonals) and character '1' are
retained from the source; grid is not modified.
'''
