class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Helper function to find the maximum subtree sum
def findLargestSubtreeSumUtil(root, maxSum):
    # Base case: if the current node is None, return 0 as sum
    if not root:
        return 0
    # Calculate the sum of nodes in the left and right subtrees
    leftSubtreeSum = findLargestSubtreeSumUtil(root.left, maxSum)
    rightSubtreeSum = findLargestSubtreeSumUtil(root.right, maxSum)
    # Sum of the current subtree rooted at this node
    currentSubtreeSum = root.data + leftSubtreeSum + rightSubtreeSum
    maxSum[0] = max(maxSum[0], currentSubtreeSum)
    # Return the current subtree sum to the parent call
    return currentSubtreeSum


def findLargestSubtreeSum(root):
    maxSum = [float("-inf")]
    # Recursively calculate subtree sums
    findLargestSubtreeSumUtil(root, maxSum)
    return maxSum[0]


def main():
    root = Node(1)
    root.left = Node(-2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(-6)
    root.right.right = Node(2)
    result = findLargestSubtreeSum(root)
    print("Largest subtree sum is:", result)


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n): each node is processed once with O(1) work per visit.
Space: O(h) auxiliary for recursion: O(log n) on balanced trees and
O(n) on skewed trees. No new result tree is allocated.
Returning subtree totals avoids rescanning descendants for every root.
The negative-infinity initial maximum handles all-negative trees; empty
input retains a sentinel (-infinity) because there is no nonempty subtree.
'''
