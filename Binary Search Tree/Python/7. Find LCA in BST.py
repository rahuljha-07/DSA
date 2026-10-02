class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def findLCAHelper(root, n1, n2):
    if not root:
        return None
    if root.data > n1 and root.data > n2:
        return findLCAHelper(root.left, n1, n2)
    elif root.data < n1 and root.data < n2:
        return findLCAHelper(root.right, n1, n2)
    return root


def findLCA(root, n1, n2):
    return findLCAHelper(root, n1, n2)


def main():
    root = Node(5)
    root.left = Node(3)
    root.right = Node(8)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(9)
    n1 = 2
    n2 = 4
    lca = findLCA(root, n1, n2)
    print(f"LCA of {n1} and {n2} is {lca.data}" if lca else "LCA not found.")


if __name__ == "__main__":
    main()


'''
Let h be tree height and n the node count.
Time: O(h): both keys choose the same child until their paths split.
Space: O(h) auxiliary for that recursive path: O(log n) when balanced,
O(n) when skewed. As in the source, both queried values must exist.
'''
