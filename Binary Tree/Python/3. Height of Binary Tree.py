class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def calculateHeight(root, currentHeight, maxHeight):
    if root is None:
        maxHeight[0] = max(maxHeight[0], currentHeight - 1)
        return
    calculateHeight(root.left, currentHeight + 1, maxHeight)
    calculateHeight(root.right, currentHeight + 1, maxHeight)


def heightTopDown(root):
    maxHeight = [0]
    calculateHeight(root, 1, maxHeight)
    return maxHeight[0]


def calculateHeightBottomUp(root):
    if root is None:
        return 0
    leftHeight = calculateHeightBottomUp(root.left)
    rightHeight = calculateHeightBottomUp(root.right)
    return 1 + max(leftHeight, rightHeight)


def height(root):
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
