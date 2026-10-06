class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.maxDiameter = 0

    # Helper function to calculate the height of the tree and update the diameter
    def calculateHeight(self, root):
        # If the node is None, return height as 0
        if not root:
            return 0
        # Recursively calculate the height of the left and right subtrees
        leftHeight = self.calculateHeight(root.left)
        rightHeight = self.calculateHeight(root.right)
        # The height of the current node is the maximum of the left and right subtrees plus
        # 1
        currentHeight = max(leftHeight, rightHeight) + 1
        # Calculate the diameter at the current node (sum of left and right heights)
        currentDiameter = leftHeight + rightHeight + 1
        # Update the maximum diameter if the current diameter is larger
        self.maxDiameter = max(self.maxDiameter, currentDiameter)
        # Return the height of the current node
        return currentHeight

    def diameter(self, root):
        # Initialize the maximum diameter to zero
        self.maxDiameter = 0
        # Start the recursive calculation
        self.calculateHeight(root)
        # Return the maximum diameter found
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
