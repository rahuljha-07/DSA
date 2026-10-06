class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def findValue(root, target):
    # Base case: if root is None, target is not in the tree
    if root is None:
        return False
    if root.val == target:
        return True
    if target < root.val:
        return findValue(root.left, target)
    # Otherwise, search the right subtree
    else:
        return findValue(root.right, target)


def main():
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.right.right = TreeNode(14)
    target = 6
    if findValue(root, target):
        print(f"Value {target} found in the BST.")
    else:
        print(f"Value {target} not found in the BST.")


if __name__ == "__main__":
    main()


'''
Let h be tree height and n its node count.
Time: O(h): comparisons select just one child per level, not both subtrees.
Space: O(h) auxiliary: one recursive call waits per level of that path.
For a balanced BST h = O(log n); for a skewed BST h = O(n).
'''
