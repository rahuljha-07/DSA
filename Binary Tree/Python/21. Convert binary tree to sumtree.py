class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Function to convert the tree to a sum tree
def convertToSumTree(root):
    # Base case: If the node is None, return 0
    if not root:
        return 0
    # Recursively calculate the sum of the left and right subtrees
    leftSum = convertToSumTree(root.left)
    rightSum = convertToSumTree(root.right)
    # Store the original value of the current node
    originalValue = root.data
    # Update the node's value to the sum of its left and right subtree sums
    root.data = leftSum + rightSum
    # Return the total sum including the original value of the node
    return originalValue + root.data


'''
Let n be the node count and h tree height.
Time: O(n): each node is processed once with O(1) work per visit.
Space: O(h) auxiliary for recursion: O(log n) on balanced trees and
O(n) on skewed trees. No new result tree is allocated.
Each call returns its ORIGINAL subtree sum while storing the sum of
descendants in its node. Leaves become zero; the tree is changed in place.
'''
