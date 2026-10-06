class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Helper function to print a path
def printPath(path):
    for val in path:
        print(val, end=" ")
    print()


# Recursive DFS function to find paths with sum = k
def findKSumPaths(root, path, k, currentSum):
    if not root:
        return
    # Add the current node to the path and update the sum
    path.append(root.data)
    currentSum += root.data
    # Check if the sum of the current path equals k
    if currentSum == k:
        # Print the path
        printPath(path)
    # Explore left and right subtrees
    findKSumPaths(root.left, path, k, currentSum)
    findKSumPaths(root.right, path, k, currentSum)
    path.pop()


# Function to start the process for all nodes in the tree
def printAllKSumPaths(root, k):
    if not root:
        return
    # Temporary list to store the current path
    path = []
    # Start the DFS traversal from the current node
    findKSumPaths(root, path, k, 0)
    # Recursively check for paths starting at the left and right subtrees
    printAllKSumPaths(root.left, k)
    printAllKSumPaths(root.right, k)


# Wrapper function to initialize parameters and call the core logic
def printPathsWithSum(root, k):
    print(f"Paths with sum {k} are:")
    printAllKSumPaths(root, k)


def main():
    root = Node(1)
    root.left = Node(3)
    root.right = Node(-1)
    root.left.left = Node(2)
    root.left.right = Node(1)
    root.right.left = Node(4)
    root.right.right = Node(5)
    root.left.right.left = Node(1)
    root.right.left.left = Node(1)
    root.right.right.right = Node(2)
    root.right.right.right.right = Node(6)
    k = 5
    printPathsWithSum(root, k)


if __name__ == "__main__":
    main()


'''
Let n be the node count, h tree height, and P the total printed values.
Time: O(n*h + P): start a descendant traversal at EVERY node. Each node
is revisited once for each ancestor, at most h times. Printing matching
paths adds their lengths. Worst-case traversal is O(n^2) for a chain.
Space: O(h) auxiliary for recursion and the current backtracked path;
paths are printed immediately, not stored. Outer calls hold emptied
path lists while the current subtree is processed.
'''
