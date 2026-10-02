class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def findLCAHelper(root, n1, n2):
    if not root:
        return None
    if root.data == n1 or root.data == n2:
        return root
    leftLCA = findLCAHelper(root.left, n1, n2)
    rightLCA = findLCAHelper(root.right, n1, n2)
    if leftLCA and rightLCA:
        return root
    return leftLCA if leftLCA else rightLCA


def findLCA(root, n1, n2):
    return findLCAHelper(root, n1, n2)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    n1 = 4
    n2 = 5
    lca = findLCA(root, n1, n2)
    print(f"LCA of {n1} and {n2} is {lca.data}" if lca else "LCA not found.")


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n): each node is processed once with O(1) work per visit.
Space: O(h) auxiliary for recursion: O(log n) on balanced trees and
O(n) on skewed trees. No new result tree is allocated.
This is a general binary tree, so both branches may need searching.
As in the source, keys are assumed unique and both targets present;
if only one exists, that node is returned without detecting the absence.
'''
