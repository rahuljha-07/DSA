class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Recursive Preorder Traversal
def preorderRecursive(root):
    if root is None:
        return
    # Visit the node
    print(root.data, end=" ")
    # Traverse left subtree
    preorderRecursive(root.left)
    # Traverse right subtree
    preorderRecursive(root.right)


# Iterative Preorder Traversal
def preorderIterative(root):
    if root is None:
        return
    # Push the root to the stack
    st = [root]
    while st:
        # Get the top node from the stack
        # Pop the node from the stack
        current = st.pop()
        print(current.data, end=" ")
        if current.right:
            st.append(current.right)
        if current.left:
            st.append(current.left)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Preorder traversal (Recursive): ", end="")
    preorderRecursive(root)
    print()


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n): each node is visited once, or pushed/popped once in the
iterative method. Right-before-left pushes make left process first.
Space: O(h) auxiliary upper bound for recursion or pending stack branches.
Values are printed, not accumulated in a result list.
'''
