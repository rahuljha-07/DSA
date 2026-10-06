class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Helper function to perform inorder traversal and count nodes within the given range [l, h]
def inorder(root, l, h, count):
    # Base case: if the current node is None, return
    if not root:
        return
    # Traverse the left subtree
    inorder(root.left, l, h, count)
    if l <= root.data <= h:
        # Increment the count if the value is within the range
        count[0] += 1
    # Traverse the right subtree
    inorder(root.right, l, h, count)


# Function to count nodes in the BST whose values are within the range [l, h]
def getCount(root, l, h):
    # Initialize count to 0
    count = [0]
    # Call inorder traversal to count nodes in the range
    inorder(root, l, h, count)
    # Return the total count
    return count[0]


def main():
    root = Node(5)
    root.left = Node(3)
    root.right = Node(8)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(9)
    l = 4
    h = 8
    count = getCount(root, l, h)
    print(f"The number of nodes in the range [{l}, {h}] is: {count}")


if __name__ == "__main__":
    main()


'''
Let n be the node count and H tree height.
Time: O(n): the source visits both children of every node rather than
pruning branches outside [l, h]. Each range comparison is O(1).
Space: O(H) auxiliary for recursion plus a one-item count holder.
'''
