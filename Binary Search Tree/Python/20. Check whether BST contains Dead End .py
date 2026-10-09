class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Helper function to recursively check for dead ends in the BST
def checkDeadEnd(root, minVal, maxVal, hasDeadEnd):
    # Base case
    if not root or hasDeadEnd[0]:
        return

    # Step 1: Recursively check left and right subtrees
    checkDeadEnd(root.left, minVal, root.data - 1, hasDeadEnd)
    checkDeadEnd(root.right, root.data + 1, maxVal, hasDeadEnd)

    # Step 2: Check if current node is a leaf
    if not root.left and not root.right:
        # No valid integer can be inserted here
        if minVal == maxVal:
            hasDeadEnd[0] = True
            return


def isDeadEnd(root):
    # Flag to track if a dead end is found
    hasDeadEnd = [False]
    # Initial call with the full range
    mini = 1
    maxi = float('inf')

    checkDeadEnd(root, mini, maxi, hasDeadEnd)
    # Return the result (true if a dead end is found, false otherwise)
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
