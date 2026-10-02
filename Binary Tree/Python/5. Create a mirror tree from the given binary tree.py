class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def mirror(root):
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    if root.left:
        mirror(root.left)
    if root.right:
        mirror(root.right)
    return root


def mirrorBottomUp(root):
    if root is None:
        return None
    leftMirror = mirrorBottomUp(root.left)
    rightMirror = mirrorBottomUp(root.right)
    root.left = rightMirror
    root.right = leftMirror
    return root


def createMirror(root):
    mirrorBinaryTree = mirror(root)
    return mirrorBinaryTree


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print("Original tree (Inorder): ", end="")
    inorder(root)
    print()
    mirrorRoot = createMirror(root)
    print("Mirror tree (Inorder): ", end="")
    inorder(mirrorRoot)
    print()


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n): each node is processed once with O(1) work per visit.
Space: O(h) auxiliary for recursion: O(log n) on balanced trees and
O(n) on skewed trees. No new result tree is allocated.
Both mirror alternatives swap existing child pointers in place, one
before recursion and one after recursion; neither copies the tree.
'''
