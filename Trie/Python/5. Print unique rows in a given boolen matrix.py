def uniqueRow(M, row, col):
    res = []
    s = set()
    for i in range(row):
        v = []
        for j in range(col):
            v.append(M[i][j])
        key = tuple(v)
        if key not in s:
            res.append(v)
            s.add(key)
    return res


class TriNode:
    def __init__(self):
        self.children = [None] * 2
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TriNode()

    def insert(self, row):
        node = self.root
        for c in row:
            index = ord(c) - ord('0')
            if node.children[index] is None:
                node.children[index] = TriNode()
            node = node.children[index]
        if node.isEnd:
            return False
        node.isEnd = True
        return True


def findUniqueRows(row, col, matrix):
    trie = Trie()
    uniqueRows = []
    for i in range(row):
        rowStr = ""
        for j in range(col):
            rowStr += str(matrix[i][j])
        if trie.insert(rowStr):
            uniqueRows.append(rowStr)
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
