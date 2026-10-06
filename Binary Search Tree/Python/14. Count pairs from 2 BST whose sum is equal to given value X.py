class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    # Function to count pairs from two BSTs whose sum is equal to given value X
    def countPairs(self, root1, root2, X):
        # Handle edge case when either BST is empty
        if not root1 or not root2:
            return 0
        elements = set()
        self.storeElementsInSet(root1, elements)
        # Step 2: Traverse the second BST and count pairs that sum to X
        count = [0]
        self.countPairsWithSet(root2, elements, X, count)
        return count[0]

    # Helper function to traverse the first BST and store elements in a hash set
    def storeElementsInSet(self, root, elements):
        if not root:
            return
        self.storeElementsInSet(root.left, elements)
        elements.add(root.data)
        self.storeElementsInSet(root.right, elements)

    # Helper function to traverse the second BST and find pairs that sum to X
    def countPairsWithSet(self, root, elements, X, count):
        if not root:
            return
        self.countPairsWithSet(root.left, elements, X, count)
        if X - root.data in elements:
            count[0] += 1
        self.countPairsWithSet(root.right, elements, X, count)


# Helper function to create a simple BST (for testing)
def insertBST(root, key):
    if not root:
        return Node(key)
    if key < root.data:
        root.left = insertBST(root.left, key)
    else:
        root.right = insertBST(root.right, key)
    return root


def main():
    root1 = None
    root1 = insertBST(root1, 5)
    insertBST(root1, 3)
    insertBST(root1, 7)
    insertBST(root1, 2)
    insertBST(root1, 4)
    root2 = None
    root2 = insertBST(root2, 10)
    insertBST(root2, 6)
    insertBST(root2, 15)
    insertBST(root2, 3)
    insertBST(root2, 8)
    targetSum = 9
    solution = Solution()
    pairCount = solution.countPairs(root1, root2, targetSum)
    print(f"Number of pairs with sum {targetSum}: {pairCount}")


if __name__ == "__main__":
    main()


'''
Let n/m be node counts and h1/h2 the two heights.
Time: O(n + m) expected: visit both trees once; set insertion/lookups
average O(1). Hash collisions can worsen the bound.
Space: O(n + max(h1, h2)) auxiliary for elements and recursion.
Like the source, first-tree duplicates collapse in the set, so counting
all node-pair multiplicities assumes unique keys in the first BST.
'''
