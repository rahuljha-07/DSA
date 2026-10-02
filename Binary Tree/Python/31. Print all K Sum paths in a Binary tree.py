class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def printPath(path):
    for val in path:
        print(val, end=" ")
    print()


def findKSumPaths(root, path, k, currentSum):
    if not root:
        return
    path.append(root.data)
    currentSum += root.data
    if currentSum == k:
        printPath(path)
    findKSumPaths(root.left, path, k, currentSum)
    findKSumPaths(root.right, path, k, currentSum)
    path.pop()


def printAllKSumPaths(root, k):
    if not root:
        return
    path = []
    findKSumPaths(root, path, k, 0)
    printAllKSumPaths(root.left, k)
    printAllKSumPaths(root.right, k)


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
