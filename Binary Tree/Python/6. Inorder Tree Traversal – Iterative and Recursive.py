class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Recursive Inorder Traversal
def inorderRecursive(root):
    if root is None:
        return
    # Traverse left subtree
    inorderRecursive(root.left)
    # Visit node
    print(root.data, end=" ")
    # Traverse right subtree
    inorderRecursive(root.right)


# Iterative Inorder Traversal
def inorderIterative(root):
    st = []
    current = root
    while current is not None or st:
        # Reach the leftmost node of the current node
        while current is not None:
            st.append(current)
            current = current.left
        # Current must be None, so pop from the stack
        current = st.pop()
        # Visit the node
        print(current.data, end=" ")
        # Visit the right subtree
        current = current.right


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Inorder traversal (Recursive): ", end="")
    inorderRecursive(root)
    print()


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n) for both methods: recursive visits occur once per node;
iterative nodes are each pushed and popped once, so nested loops are linear.
Space: O(h) auxiliary for either the recursion stack or explicit st.
Values are printed immediately rather than stored as an O(n) result.
'''
