class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


memo = {}


# Recursive function to find the maximum sum of non-adjacent nodes
def getMaxSum(root):
    # Base case: If the current node is None, return 0 as there's no value to add
    if not root:
        return 0
    if root in memo:
        return memo[root]
    includeCurrent = root.data
    if root.left:
        includeCurrent += getMaxSum(root.left.left)
        includeCurrent += getMaxSum(root.left.right)
    if root.right:
        includeCurrent += getMaxSum(root.right.left)
        includeCurrent += getMaxSum(root.right.right)
    # Exclude the current node's value, and instead take the maximum sum of its left and
    # right subtrees
    excludeCurrent = getMaxSum(root.left) + getMaxSum(root.right)
    # Return the maximum sum for the current node
    memo[root] = max(includeCurrent, excludeCurrent)
    return memo[root]


def main():
    root = Node(10)
    root.left = Node(1)
    root.left.left = Node(2)
    root.left.right = Node(3)
    root.right = Node(4)
    root.right.right = Node(5)
    print("Maximum sum of non-adjacent nodes:", getMaxSum(root))


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n) expected on a fresh cache: memo computes each node once and
repeated child/grandchild queries become O(1) average dictionary lookups.
Space: O(n + h), hence O(n), auxiliary for memo and recursion.
Like the source, memo is global: clear it when nodes/values are mutated,
or before an independent calculation to release previously cached trees.
'''
