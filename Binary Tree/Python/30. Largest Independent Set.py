class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


dp = {}


def LIS(root):
    if root is None:
        return 0
    if root in dp:
        return dp[root]
    include = 1
    if root.left:
        include += LIS(root.left.left) + LIS(root.left.right)
    if root.right:
        include += LIS(root.right.left) + LIS(root.right.right)
    exclude = LIS(root.left) + LIS(root.right)
    dp[root] = max(include, exclude)
    return dp[root]


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
