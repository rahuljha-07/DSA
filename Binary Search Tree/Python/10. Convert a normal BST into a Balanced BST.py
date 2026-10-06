class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    # Function to balance an unbalanced BST
    def balanceBST(self, root):
        sortedNodes = []
        # Step 1: Collect nodes in sorted order
        self.inorderTraversal(root, sortedNodes)
        # Step 2: Build balanced BST
        return self.buildBalancedBST(sortedNodes, 0, len(sortedNodes) - 1)

    # Helper function to perform inorder traversal and store nodes in a sorted list
    def inorderTraversal(self, root, sortedNodes):
        if not root:
            return
        self.inorderTraversal(root.left, sortedNodes)
        sortedNodes.append(root.data)
        self.inorderTraversal(root.right, sortedNodes)

    # Helper function to construct a balanced BST from a sorted list of nodes
    def buildBalancedBST(self, sortedNodes, start, end):
        if start > end:
            return None
        # Choose the middle element as the root
        mid = (start + end) // 2
        root = Node(sortedNodes[mid])
        # Recursively build the left and right subtrees
        root.left = self.buildBalancedBST(sortedNodes, start, mid - 1)
        root.right = self.buildBalancedBST(sortedNodes, mid + 1, end)
        return root


# Helper function to print the inorder traversal of the tree (for verification)
def inorderPrint(root):
    if not root:
        return
    inorderPrint(root.left)
    print(root.data, end=" ")
    inorderPrint(root.right)


def main():
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(1)
    root.right = Node(15)
    root.right.right = Node(20)
    solution = Solution()
    balancedRoot = solution.balanceBST(root)
    print("Inorder Traversal of Balanced BST: ", end="")
    inorderPrint(balancedRoot)
    print()


if __name__ == "__main__":
    main()


'''
Let n be the node count and h the original height.
Time: O(n): inorder collects each value once; midpoint construction makes
one new node per value, with no repeated scans or sorting.
Space: O(n) auxiliary for sortedNodes plus O(h) collection/O(log n)
construction stacks. The new balanced tree needs O(n) output space.
'''
