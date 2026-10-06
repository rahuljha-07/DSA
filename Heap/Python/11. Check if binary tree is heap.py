class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Function to count the number of nodes in the binary tree
def size(root):
    # If the tree is empty, return 0
    if root is None:
        return 0
    leftsize = size(root.left)
    rightsize = size(root.right)
    # Recursively count nodes in left and right subtrees
    return 1 + leftsize + rightsize


# Helper function to check if the tree satisfies the heap property
def solve(tree, idx, n):
    # Base case: If the node is None, it's valid
    if tree is None:
        return True
    # If the current index exceeds the total number of nodes, it's not a valid heap
    if idx >= n:
        return False
    if tree.left and tree.left.data >= tree.data:
        return False
    if tree.right and tree.right.data >= tree.data:
        return False
    # Recursively check the left and right subtrees
    return (solve(tree.left, 2 * idx + 1, n)
            and solve(tree.right, 2 * idx + 2, n))


# Function to check if a binary tree is a max-heap
def isHeap(tree):
    # An empty tree is trivially a heap
    if tree is None:
        return True
    # Get the total number of nodes in the tree
    n = size(tree)
    # Start from the root with index 0
    idx = 0
    # Check if the tree satisfies both the complete binary tree and max-heap properties
    return solve(tree, idx, n)


def main():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(1)
    print("The binary tree is a max-heap." if isHeap(root)
          else "The binary tree is not a max-heap.")


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n): size visits all nodes, then solve checks completeness indices
and heap order at most once per node. Two passes add to O(n).
Space: O(h) auxiliary for recursion; no node array or BFS queue is stored.
The source's STRICT order is retained: equal parent/child values fail,
although conventional max-heaps permit equality.
'''
