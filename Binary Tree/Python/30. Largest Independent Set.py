class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


dp = {}


# Function to calculate LIS for the binary tree
def LIS(root):
    # Base Case: If the node is None, LIS is 0
    if root is None:
        return 0
    if root in dp:
        return dp[root]
    # Case 1: Include the current node in LIS
    include = 1
    if root.left:
        # Add LIS of left-left and left-right (grandchildren)
        # Add LIS of right-left and right-right (grandchildren)
        include += LIS(root.left.left) + LIS(root.left.right)
    if root.right:
        include += LIS(root.right.left) + LIS(root.right.right)
    # Case 2: Exclude the current node from LIS
    # Add LIS of immediate children (left and right)
    exclude = LIS(root.left) + LIS(root.right)
    # Return the computed value of Store the maximum of include and exclude in dp
    dp[root] = max(include, exclude)
    return dp[root]


# Helper function to free the dynamically allocated memory
def deleteTree(root):
    if root is None:
        return
    deleteTree(root.left)
    deleteTree(root.right)
    dp.pop(root, None)
    root.left = None
    root.right = None


def main():
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.right = Node(60)
    root.left.right.left = Node(70)
    root.left.right.right = Node(80)
    print("Size of the Largest Independent Set:", LIS(root))
    deleteTree(root)


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n) expected on a fresh dp cache: each node's include/exclude
result is computed once; later requests are O(1) average lookups.
Space: O(n + h), hence O(n), auxiliary for memoized results and recursion.
deleteTree takes O(n) time/O(h) stack to detach links and drop cache entries;
Python reclaims unreferenced objects rather than using C++ delete.
Clear global dp before recomputing after any structural mutation.
'''
