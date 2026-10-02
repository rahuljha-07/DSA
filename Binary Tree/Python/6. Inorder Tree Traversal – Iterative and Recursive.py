class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def inorderRecursive(root):
    if root is None:
        return
    inorderRecursive(root.left)
    print(root.data, end=" ")
    inorderRecursive(root.right)


def inorderIterative(root):
    st = []
    current = root
    while current is not None or st:
        while current is not None:
            st.append(current)
            current = current.left
        current = st.pop()
        print(current.data, end=" ")
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
