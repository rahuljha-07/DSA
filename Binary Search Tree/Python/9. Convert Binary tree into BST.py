class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Helper function to perform an in-order traversal of the tree and store the values in a
# list
def inOrderTraversal(root, values):
    # Base case: if the node is None, do nothing
    if not root:
        return
    # Traverse the left subtree
    inOrderTraversal(root.left, values)
    # Add the node's data to the list
    values.append(root.data)
    # Traverse the right subtree
    inOrderTraversal(root.right, values)


# Helper function to perform an in-order traversal of the tree and assign sorted values from
# the list
def assignSortedValues(root, values):
    if not root:
        return
    assignSortedValues(root.left, values)
    # Assign the current node the next sorted value from the list
    root.data = values[0]
    values.pop(0)
    assignSortedValues(root.right, values)


def binaryTreeToBST(root):
    values = []
    # Step 1: Perform an in-order traversal of the binary tree to collect all values
    inOrderTraversal(root, values)
    # Step 2: Sort the values to ensure they can form a BST
    values.sort()
    # Step 3: Assign the sorted values back to the tree nodes in in-order traversal
    assignSortedValues(root, values)
    # Return the root of the modified tree, now a BST
    return root


def main():
    root = Node(10)
    root.left = Node(30)
    root.right = Node(20)
    root.left.left = Node(40)
    root.left.right = Node(60)
    root.right.left = Node(50)
    root.right.right = Node(70)
    root = binaryTreeToBST(root)
    values = []
    inOrderTraversal(root, values)
    print("Inorder Traversal of Converted BST:", *values)


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n^2): collection is O(n), sorting O(n log n), but pop(0) shifts
the remaining values on every assignment. n-1 + n-2 + ... shifts dominate.
Space: O(n + h) auxiliary, hence O(n), for values, sorting workspace,
and recursion. Tree shape is retained and existing nodes are reused.
'''
