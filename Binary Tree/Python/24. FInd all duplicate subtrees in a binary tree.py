class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


subtreeMap = {}
duplicateRoots = []


# Helper function to serialize subtrees and check for duplicates
def findDuplicateSubtreesUtil(root):
    # Use "#" to represent None nodes to avoid ambiguity
    if not root:
        return "#"
    # Serialize left and right subtrees separately
    leftString = findDuplicateSubtreesUtil(root.left)
    rightString = findDuplicateSubtreesUtil(root.right)
    # Form the final subtree string
    subtree = str(root.data) + "," + leftString + "," + rightString
    # If this subtree has already appeared once, add its root to duplicateRoots
    if subtreeMap.get(subtree, 0) == 1:
        duplicateRoots.append(root)
    subtreeMap[subtree] = subtreeMap.get(subtree, 0) + 1
    return subtree


def findDuplicateSubtrees(root):
    # Clear the map before starting
    subtreeMap.clear()
    # Clear the duplicates list before starting
    duplicateRoots.clear()
    # Populate the map and collect duplicate roots
    findDuplicateSubtreesUtil(root)
    # Return all root nodes of duplicate subtrees
    return list(duplicateRoots)


# Helper function to print a subtree rooted at the given node
def printSubtree(root):
    if not root:
        return
    print(root.data, end=" ")
    printSubtree(root.left)
    printSubtree(root.right)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(2)
    root.right.left.left = Node(4)
    root.right.right = Node(4)
    duplicates = findDuplicateSubtrees(root)
    print("Duplicate Subtrees:")
    for duplicateRoot in duplicates:
        printSubtree(duplicateRoot)
        print()


if __name__ == "__main__":
    main()


'''
Let n be the node count, h tree height, and S the sum of all serialized
subtree lengths (assuming bounded-length integer labels).
Time: O(S) expected: building and hashing each string costs its length,
not O(1). S is O(n*h): O(n log n) when balanced, O(n^2) when skewed.
Space: O(S + h) auxiliary for stored string keys and recursion, plus
O(d) output pointers for d duplicate patterns. Leaves count as subtrees.
Each duplicated pattern is added only on its second occurrence.
'''
