class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def findMaxSumPath(root, currentLength, maxLength, currentSum, maxSum):
    if not root:
        return 0
    leftSum = findMaxSumPath(root.left, currentLength + 1, maxLength,
                             currentSum + root.data, maxSum)
    rightSum = findMaxSumPath(root.right, currentLength + 1, maxLength,
                              currentSum + root.data, maxSum)
    if not root.left and not root.right:
        if currentLength > maxLength[0]:
            maxLength[0] = currentLength
            maxSum[0] = currentSum + root.data
        elif currentLength == maxLength[0]:
            maxSum[0] = max(maxSum[0], currentSum + root.data)
    return max(leftSum, rightSum)


def sumOfLongRootToLeafPath(root):
    if not root:
        return 0
    maxLength = [0]
    maxSum = [float("-inf")]
    findMaxSumPath(root, 1, maxLength, 0, maxSum)
    return maxSum[0]


def main():
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(7)
    root.left.right = Node(1)
    root.right.left = Node(2)
    root.right.right = Node(3)
    root.left.right.left = Node(6)
    result = sumOfLongRootToLeafPath(root)
    print("Maximum sum of nodes on the longest path from root to leaf:", result)


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n): each node is processed once with O(1) work per visit.
Space: O(h) auxiliary for recursion: O(log n) on balanced trees and
O(n) on skewed trees. No new result tree is allocated.
Length and sum travel down the recursion without copying whole paths.
A longer path REPLACES the previous best sum; equal-length paths compare
sums. Starting currentSum at zero counts the root once and supports negatives.
'''
