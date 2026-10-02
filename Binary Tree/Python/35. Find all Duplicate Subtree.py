class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


subtreeMap = {}


def serializeSubtree(root):
    if not root:
        return "$"
    leftString = serializeSubtree(root.left)
    rightString = serializeSubtree(root.right)
    subtree = leftString + "," + str(root.data) + "," + rightString
    subtreeMap[subtree] = subtreeMap.get(subtree, 0) + 1
    return subtree


def hasDuplicateSubtree(root):
    subtreeMap.clear()
    serializeSubtree(root)
    for entry in subtreeMap.values():
        if entry >= 2:
            return True
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
