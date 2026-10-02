class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder):
        return self.helper(preorder, 0, len(preorder))

    def helper(self, preorder, rootIndex, rightLimit):
        if rootIndex >= rightLimit:
            return None
        value = preorder[rootIndex]
        root = Node(value)
        i = rootIndex + 1
        while i < rightLimit and preorder[i] < value:
            i += 1
        root.left = self.helper(preorder, rootIndex + 1, i)
        root.right = self.helper(preorder, i, rightLimit)
        return root


def inorderTraversal(root):
    if not root:
        return
    inorderTraversal(root.left)
    print(root.data, end=" ")
    inorderTraversal(root.right)


def main():
    preorder = [40, 30, 35, 80, 100]
    solution = Solution()
    root = solution.bstFromPreorder(preorder)
    print("Inorder Traversal of the Constructed BST: ", end="")
    inorderTraversal(root)
    print()


if __name__ == "__main__":
    main()


'''
Let n be the preorder length and h the constructed height.
Time: O(n^2) worst case: each root scans its remaining range for the first
larger value; decreasing input gives scans of n-1, n-2, ... . Balanced
partitions cost O(n log n); increasing input needs only O(n).
Space: O(h) auxiliary for recursion, plus O(n) output nodes. Index ranges
avoid copied slices. Input is assumed to be valid BST preorder.
'''
