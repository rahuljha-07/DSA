class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    # Function to construct BST from the given preorder traversal array
    def bstFromPreorder(self, preorder):
        # Start with the entire range
        return self.helper(preorder, 0, len(preorder))

    # Helper function to recursively build the BST
    def helper(self, preorder, rootIndex, rightLimit):
        # Base case: if we've reached the end of the array, return None
        if rootIndex >= rightLimit:
            return None
        # Get the value of the current root node from the preorder array
        value = preorder[rootIndex]
        root = Node(value)
        # Find the right child index (first value greater than current node value)
        i = rootIndex + 1
        while i < rightLimit and preorder[i] < value:
            # Move to the right if the value is smaller than the current root
            i += 1
        # Recursively build the left and right subtrees
        # Left subtree: nodes smaller than root
        root.left = self.helper(preorder, rootIndex + 1, i)
        # Right subtree: nodes greater than root
        root.right = self.helper(preorder, i, rightLimit)
        # Return the root node
        return root


# Helper function to print the inorder traversal of the tree (for verification)
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
