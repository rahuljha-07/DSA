class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Helper function to mirror a single node (swap its left and right children)
# top down approach
def mirror(root):
    if root is None:
        return None
    # Use swap to swap the left and right children
    root.left, root.right = root.right, root.left
    if root.left:
        mirror(root.left)
    if root.right:
        mirror(root.right)
    return root


# bottom up
def mirrorBottomUp(root):
    if root is None:
        return None
    # Recursively mirror the left and right subtrees
    leftMirror = mirrorBottomUp(root.left)
    rightMirror = mirrorBottomUp(root.right)
    # Swap the mirrored subtrees
    root.left = rightMirror
    root.right = leftMirror
    return root


# Function to create a mirror of the binary tree
def createMirror(root):
    # Call the helper function to mirror the tree
    mirrorBinaryTree = mirror(root)
    # Return the root of the mirrored tree
    return mirrorBinaryTree


# Function to print inorder traversal of the tree (to check the result)
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
