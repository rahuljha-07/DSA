class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


subtreeMap = {}


# Helper function to serialize subtrees and check for duplicates
def serializeSubtree(root):
    # Base case: if the node is None, return a unique symbol to represent it
    if not root:
        return "$"
    # Serialize the left and right subtrees separately
    leftString = serializeSubtree(root.left)
    rightString = serializeSubtree(root.right)
    # Create the subtree representation
    subtree = leftString + "," + str(root.data) + "," + rightString
    subtreeMap[subtree] = subtreeMap.get(subtree, 0) + 1
    return subtree


def hasDuplicateSubtree(root):
    # Clear the map before starting
    subtreeMap.clear()
    # Serialize the entire tree
    serializeSubtree(root)
    # Check if any subtree appears more than once
    for entry in subtreeMap.values():
        # Duplicate subtree found
        if entry >= 2:
            return True
    # No duplicate subtrees
    return False


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(2)
    root.right.left.left = Node(4)
    root.right.right = Node(4)
    print("Does the tree have a duplicate subtree?",
          "Yes" if hasDuplicateSubtree(root) else "No")


if __name__ == "__main__":
    main()


'''
Let n be the node count, h tree height, and S the sum of serialized
subtree lengths, assuming bounded-length integer labels.
Time: O(S) expected: string concatenation/hashing costs each string's
length. S = O(n*h), or O(n^2) for a skewed tree; scanning counts adds O(n).
Space: O(S + h) auxiliary for string keys and recursion.
Like the source, identical leaves count as duplicate subtrees too.
'''
