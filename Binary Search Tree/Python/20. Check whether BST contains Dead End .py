class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def checkDeadEnd(root, minVal, maxVal, hasDeadEnd):
    if not root or hasDeadEnd[0]:
        return
    if not root.left and not root.right:
        if minVal == maxVal:
            hasDeadEnd[0] = True
            return
    checkDeadEnd(root.left, minVal, root.data - 1, hasDeadEnd)
    checkDeadEnd(root.right, root.data + 1, maxVal, hasDeadEnd)


def isDeadEnd(root):
    hasDeadEnd = [False]
    checkDeadEnd(root, 1, 2147483647, hasDeadEnd)
    return hasDeadEnd[0]


def main():
    root = Node(8)
    root.left = Node(5)
    root.right = Node(9)
    root.left.left = Node(2)
    root.left.right = Node(7)
    root.left.left.left = Node(1)
    print("BST contains dead end?", "Yes" if isDeadEnd(root) else "No")


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n) worst case: each node's allowed integer range is examined once;
finding a dead end can stop traversal early.
Space: O(h) auxiliary for recursive calls and a constant-size flag holder.
The source's key domain is retained: integers from 1 through INT_MAX.
'''
