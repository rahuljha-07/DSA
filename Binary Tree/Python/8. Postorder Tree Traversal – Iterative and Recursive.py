class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Recursive Postorder Traversal (Left, Right, Root)
def postorderRecursive(root):
    if root is None:
        return
    # Recursively visit left subtree
    postorderRecursive(root.left)
    # Recursively visit right subtree
    postorderRecursive(root.right)
    # Visit the root node
    print(root.data, end=" ")


# Iterative Postorder Traversal (using one stack and a list)
def postorderIterative(root):
    if root is None:
        return
    st1 = [root]
    # To store the postorder traversal
    result = []
    while st1:
        current = st1.pop()
        # Store the node data in the list
        result.append(current.data)
        if current.left:
            st1.append(current.left)
        if current.right:
            st1.append(current.right)
    # Reverse the list to get the correct postorder sequence
    result.reverse()
    # Print the postorder traversal
    for data in result:
        print(data, end=" ")


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Postorder traversal (Recursive): ", end="")
    postorderRecursive(root)
    print()


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n) for both: one visit per node. Iterative reversal/printing add
two linear passes, not a multiplicative factor.
Recursive space: O(h) auxiliary. Iterative space: O(n) auxiliary because
result stores ALL node values before printing, besides the explicit stack.
'''
