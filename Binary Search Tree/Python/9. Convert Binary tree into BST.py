class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def inOrderTraversal(root, values):
    if not root:
        return
    inOrderTraversal(root.left, values)
    values.append(root.data)
    inOrderTraversal(root.right, values)


def assignSortedValues(root, values):
    if not root:
        return
    assignSortedValues(root.left, values)
    root.data = values[0]
    values.pop(0)
    assignSortedValues(root.right, values)


def binaryTreeToBST(root):
    values = []
    inOrderTraversal(root, values)
    values.sort()
    assignSortedValues(root, values)
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
