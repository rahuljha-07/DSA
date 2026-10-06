dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


# Helper function to check if the word exists starting at (x, y) in direction (dx, dy)
def searchInDirection(grid, word, x, y, dir):
    n = len(grid)
    m = len(grid[0])
    k = len(word)

    for i in range(k):
        newX = x + i * dx[dir]
        newY = y + i * dy[dir]

        # Out of bounds or character mismatch
        if newX < 0 or newY < 0 or newX >= n or newY >= m or grid[newX][newY] != word[i]:
            return False
    # Word matched in this direction
    return True


def searchWord(grid, word):
    n = len(grid)
    m = len(grid[0])
    result = []

    for i in range(n):
        for j in range(m):
            # Start searching if the first character matches
            if grid[i][j] == word[0]:
                for dir in range(8):
                    if searchInDirection(grid, word, i, j, dir):
                        result.append((i, j))
                        # Avoid duplicates from different directions
                        break

    # Sort result to ensure lexicographical order
    result.sort()
    return result


# KMP
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


# KMP search algorithm to find occurrences and their starting coordinates
def kmpSearch(text, pattern, row, col):
    prefixTable = buildPrefixTable(pattern)
    coordinates = []
    # Index for pattern
    j = 0

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = prefixTable[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            # Store the starting coordinate
            coordinates.append((row, col + i - j + 1))
            # Reset j for the next potential match
            j = prefixTable[j - 1]
    return coordinates


# Function to search for the pattern in all directions in the 2D array
def findOccurrences(grid, str):
    rows = len(grid)
    cols = len(grid[0])
    pattern = str
    result = []

    # Search horizontally (left to right and right to left)
    for i in range(rows):
        rowText = ""
        for j in range(cols):
            rowText += grid[i][j]
        result.extend(kmpSearch(rowText, pattern, i, 0))

        rowText = rowText[::-1]
        result.extend(kmpSearch(rowText, pattern, i, cols - 1))

    # Search vertically (top to down and down to top)
    for j in range(cols):
        colText = ""
        for i in range(rows):
            colText += grid[i][j]
        result.extend(kmpSearch(colText, pattern, 0, j))

        colText = colText[::-1]
        result.extend(kmpSearch(colText, pattern, rows - 1, j))

    # Search diagonally (down-right, down-left, up-right, up-left)
    # Down-right diagonal
    for i in range(rows):
        for j in range(cols):
            diagText = ""
            x, y = i, j
            while x < rows and y < cols:
                diagText += grid[x][y]
                x += 1
                y += 1
            result.extend(kmpSearch(diagText, pattern, i, j))

    # Down-left diagonal
    for i in range(rows):
        for j in range(cols - 1, -1, -1):
            diagText = ""
            x, y = i, j
            while x < rows and y >= 0:
                diagText += grid[x][y]
                x += 1
                y -= 1
            result.extend(kmpSearch(diagText, pattern, i, j))

    # Up-right diagonal
    for i in range(rows - 1, -1, -1):
        for j in range(cols):
            diagText = ""
            x, y = i, j
            while x >= 0 and y < cols:
                diagText += grid[x][y]
                x -= 1
                y += 1
            result.extend(kmpSearch(diagText, pattern, i, j))

    # Up-left diagonal
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            diagText = ""
            x, y = i, j
            while x >= 0 and y >= 0:
                diagText += grid[x][y]
                x -= 1
                y -= 1
            result.extend(kmpSearch(diagText, pattern, i, j))

    return result


grid = [
    ['a', 'b', 'a', 'b'],
    ['a', 'b', 'e', 'b'],
    ['e', 'b', 'e', 'b']
]
word = "abe"

occurrences = findOccurrences(grid, word)

print("Occurrences of '" + word + "':")
for coord in occurrences:
    print("{" + str(coord[0]) + ", " + str(coord[1]) + "}")


'''
Time Complexity: O(n * m * k) for directional search, where k is word length.

Reason:
The search may start from every cell in the matrix.
From each matching start, it checks up to 8 directions.
In each direction, up to k characters of the word are compared.
The constant 8 is ignored, so the bound is O(n * m * k).

Space Complexity: O(k), excluding output.

Reason:
The KMP helper uses a prefix table of size k.
Other variables are constant, and the result list is output space.
'''
