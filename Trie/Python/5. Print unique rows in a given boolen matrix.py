# without trie
# Function to find unique rows in a boolean matrix
def uniqueRow(M, row, col):
    # To store the result of unique rows
    res = []
    # Set to keep track of unique rows
    s = set()
    # Traverse each row of the matrix
    for i in range(row):
        # Create a list to store the current row
        v = []
        # Push each element of the row into the list
        for j in range(col):
            v.append(M[i][j])
        key = tuple(v)
        if key not in s:
            res.append(v)
            s.add(key)
    # Return the result list containing unique rows
    return res


class TriNode:
    def __init__(self):
        self.children = [None] * 2
        self.isEnd = False


class Trie:
    def __init__(self):
        # Initialize the root node
        self.root = TriNode()

    # Insert a binary string into the Trie
    def insert(self, row):
        node = self.root
        for c in row:
            # Convert character '0' or '1' to int 0 or 1
            index = ord(c) - ord('0')
            if node.children[index] is None:
                node.children[index] = TriNode()
            node = node.children[index]
        if node.isEnd:
            return False
        # Mark the end of this row
        node.isEnd = True
        return True


def findUniqueRows(row, col, matrix):
    trie = Trie()
    # To store the unique rows as strings
    uniqueRows = []
    for i in range(row):
        # Convert row i into a string
        rowStr = ""
        for j in range(col):
            rowStr += str(matrix[i][j])
        # Insert the row into the Trie
        if trie.insert(rowStr):
            uniqueRows.append(rowStr)
    # Output the unique rows
    for row in uniqueRows:
        for c in row:
            print(c, end=" ")
        print("$", end="")


def main():
    row = 3
    col = 4
    matrix = [[1, 1, 0, 1], [1, 0, 0, 1], [1, 1, 0, 1]]
    findUniqueRows(row, col, matrix)


if __name__ == "__main__":
    main()


'''
Let r/c be row/column counts and u unique rows.
Set method time: O(r*c) expected for row copying/tuple hashing; Python
uses a hash set rather than C++'s ordered set (no sorted iteration needed).
Space: O(u*c) auxiliary keys plus O(u*c) output rows.
Trie method time: O(r*c) trie work plus row-string construction, potentially
O(r*c^2) copying without optimized appends; printing costs O(u*c).
Space: O(r*c) worst-case auxiliary trie/string storage.
Both preserve first-occurrence order; trie inputs must contain only 0/1.
'''
