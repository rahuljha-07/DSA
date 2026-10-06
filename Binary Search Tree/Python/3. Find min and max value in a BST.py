class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Function to find the minimum value in a BST
def findMin(root):
    if root is None:
        raise ValueError("Tree is empty")
    # Traverse left until you reach the leftmost node
    while root.left is not None:
        root = root.left
    return root.data


# Function to find the maximum value in a BST
def findMax(root):
    if root is None:
        raise ValueError("Tree is empty")
    # Traverse right until you reach the rightmost node
    while root.right is not None:
        root = root.right
    return root.data


def main():
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)
    try:
        print("Minimum value in the BST:", findMin(root))
        print("Maximum value in the BST:", findMax(root))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()


'''
Let h be tree height.
Time: O(h) for either search: minimum follows only left links; maximum
follows only right links. Calling both is still O(h).
Space: O(1) auxiliary: loops update a pointer without a stack or container.
h is O(log n) for balanced trees and O(n) for skewed trees.
'''
