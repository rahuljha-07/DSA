class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.maxDiameter = 0

    def calculateHeight(self, root):
        if not root:
            return 0
        leftHeight = self.calculateHeight(root.left)
        rightHeight = self.calculateHeight(root.right)
        currentHeight = max(leftHeight, rightHeight) + 1
        currentDiameter = leftHeight + rightHeight + 1
        self.maxDiameter = max(self.maxDiameter, currentDiameter)
        return currentHeight

    def diameter(self, root):
        self.maxDiameter = 0
        self.calculateHeight(root)
        return self.maxDiameter


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    solution = Solution()
    print("Diameter of the tree:", solution.diameter(root))


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n): each node is processed once with O(1) work per visit.
Space: O(h) auxiliary for recursion: O(log n) on balanced trees and
O(n) on skewed trees. No new result tree is allocated.
Heights and diameter are computed in the SAME postorder pass, avoiding
repeated height scans. Diameter counts nodes; an empty tree returns 0.
'''
