# Function to build the prefix table for KMP algorithm
def buildPrefixTable(pattern):
    m = len(pattern)
    prefixTable = [0] * m
    # Length of the previous longest prefix suffix
    j = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefixTable[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefixTable[i] = j
    return prefixTable


# KMP search algorithm
def kmpSearch(text, pattern):
    prefixTable = buildPrefixTable(pattern)
    count = 0
    # Index for pattern
    j = 0

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = prefixTable[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            # Found an occurrence
            count += 1
            # Reset j for the next potential match
            j = prefixTable[j - 1]
    return count


# Function to search for the pattern in all directions in the 2D array
def countOccurrences(grid, str):
    rows = len(grid)
    cols = len(grid[0])
    pattern = str
    totalCount = 0

    # Search horizontally (left to right and right to left)
    for i in range(rows):
        rowText = ""
        for j in range(cols):
            rowText += grid[i][j]
        # Left to right
        # Right to left
        totalCount += kmpSearch(rowText, pattern)
        rowText = rowText[::-1]
        totalCount += kmpSearch(rowText, pattern)

    # Search vertically (top to down and down to top)
    for j in range(cols):
        colText = ""
        for i in range(rows):
            colText += grid[i][j]
        # Top to down
        # Down to top
        totalCount += kmpSearch(colText, pattern)
        colText = colText[::-1]
        totalCount += kmpSearch(colText, pattern)

    return totalCount


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# Helper function for recursive search
def searchFromCell(grid, pattern, x, y, index):
    rows = len(grid)
    cols = len(grid[0])

    # Base cases
    # Found the pattern
    if index == len(pattern):
        return 1
    if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] != pattern[index]:
        return 0

    # Mark the current cell as visited to prevent revisiting
    temp = grid[x][y]
    # Temporarily mark as visited
    grid[x][y] = '#'

    count = 0
    # Explore all 4 directions
    for dir in range(4):
        newX = x + dx[dir]
        newY = y + dy[dir]
        count += searchFromCell(grid, pattern, newX, newY, index + 1)

    # Restore the original value of the cell
    grid[x][y] = temp

    return count


def countOccurrencesInGrid(grid, pattern):
    rows = len(grid)
    cols = len(grid[0])
    totalCount = 0

    # Iterate through every cell in the matrix
    for i in range(rows):
        for j in range(cols):
            # Start recursion if the first character matches
            if grid[i][j] == pattern[0]:
                totalCount += searchFromCell(grid, pattern, i, j, 0)

    return totalCount


grid1 = [
    ['D', 'D', 'D', 'G', 'D', 'D'],
    ['B', 'B', 'D', 'E', 'B', 'S'],
    ['B', 'S', 'K', 'E', 'B', 'K'],
    ['D', 'D', 'D', 'D', 'D', 'E'],
    ['D', 'D', 'D', 'D', 'D', 'E'],
    ['D', 'D', 'D', 'D', 'D', 'G']
]
str1 = "GEEKS"
print("Output for grid1:", countOccurrences(grid1, str1))

grid2 = [
    ['B', 'B', 'M', 'B', 'B', 'B'],
    ['C', 'B', 'A', 'B', 'B', 'B'],
    ['I', 'B', 'G', 'B', 'B', 'B'],
    ['G', 'B', 'I', 'B', 'B', 'B'],
    ['A', 'B', 'C', 'B', 'B', 'B'],
    ['M', 'C', 'I', 'G', 'A', 'M']
]
str2 = "MAGIC"
print("Output for grid2:", countOccurrences(grid2, str2))


'''
Time Complexity: O(rows * cols * pattern length) for search work in the shown approaches.

Reason:
For KMP row and column search, every row and column is converted
to a string and searched using the pattern.

For recursive grid search, we may start from many cells and explore
directions according to the pattern length.
That is why the work depends on rows, cols, and pattern length.

Space Complexity: O(pattern length)

Reason:
KMP uses a prefix table of size equal to the pattern length.
The recursive approach can also use recursion depth up to the
pattern length.
'''
