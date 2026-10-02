class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def convertToSumTree(root):
    if not root:
        return 0
    leftSum = convertToSumTree(root.left)
    rightSum = convertToSumTree(root.right)
    originalValue = root.data
    root.data = leftSum + rightSum
    return originalValue + root.data


'''
Let n be the node count and h tree height.
Time: O(n): each node is processed once with O(1) work per visit.
Space: O(h) auxiliary for recursion: O(log n) on balanced trees and
O(n) on skewed trees. No new result tree is allocated.
Each call returns its ORIGINAL subtree sum while storing the sum of
descendants in its node. Leaves become zero; the tree is changed in place.
'''
