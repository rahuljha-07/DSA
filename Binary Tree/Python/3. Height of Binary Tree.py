class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Function to perform top-down traversal and calculate height
def calculateHeight(root, currentHeight, maxHeight):
    if root is None:
        maxHeight[0] = max(maxHeight[0], currentHeight - 1)
        return
    # Recursively visit left and right subtrees, increasing height by 1 for each level
    calculateHeight(root.left, currentHeight + 1, maxHeight)
    calculateHeight(root.right, currentHeight + 1, maxHeight)


# Wrapper function to calculate the height of the binary tree using top-down approach
def heightTopDown(root):
    # Variable to store the maximum height
    maxHeight = [0]
    # Start with height 1 for the root
    calculateHeight(root, 1, maxHeight)
    return maxHeight[0]


# bottom up approach
# Helper function to calculate height from the bottom-up
def calculateHeightBottomUp(root):
    if root is None:
        # Base case: If the tree is empty, return height as 0
        return 0
    # Recursively calculate the height of left and right subtrees and return the maximum
    # height + 1
    leftHeight = calculateHeightBottomUp(root.left)
    rightHeight = calculateHeightBottomUp(root.right)
    # Height is max of left and right subtrees + 1
    return 1 + max(leftHeight, rightHeight)


# Main height function that calls the helper function
def height(root):
    # Call the helper function to calculate the height and return the result
    return calculateHeightBottomUp(root)


'''
Let n be the node count and h tree height.
Time: O(n): each node is processed once with O(1) work per visit.
Space: O(h) auxiliary for recursion: O(log n) on balanced trees and
O(n) on skewed trees. No new result tree is allocated.
Both methods measure height in nodes (empty = 0, singleton = 1).
The top-down null-child depth is reduced by one to avoid the source's
off-by-one error. Its maxHeight holder adds only O(1) space.
'''
