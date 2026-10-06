class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


flag = 1


def isSumTreeUtil(root):
    global flag
    # Base case: if the node is None, return 0 as sum
    if not root:
        return 0
    if not root.left and not root.right:
        return root.data
    # If flag is set to 0, return immediately to break recursion
    if flag == 0:
        return 0
    # Recursive calls to get the sum of left and right subtrees
    leftSum = isSumTreeUtil(root.left)
    rightSum = isSumTreeUtil(root.right)
    if leftSum + rightSum != root.data:
        flag = 0
    # Return the sum of the current node and its subtrees
    return leftSum + rightSum + root.data


def isSumTree(root):
    global flag
    # Initialize flag as true (1)
    flag = 1
    isSumTreeUtil(root)
    return bool(flag)


'''
Let n be the node count and h tree height.
Time: O(n): each node is processed once with O(1) work per visit.
Space: O(h) auxiliary for recursion: O(log n) on balanced trees and
O(n) on skewed trees. No new result tree is allocated.
Postorder returns subtree sums while checking each non-leaf node; sums
are not recomputed by extra traversals. flag is shared, not shadowed by
a local variable, and the helper returns numeric sums rather than bools.
'''
