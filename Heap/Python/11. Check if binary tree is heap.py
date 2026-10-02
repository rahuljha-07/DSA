class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def size(root):
    if root is None:
        return 0
    leftsize = size(root.left)
    rightsize = size(root.right)
    return 1 + leftsize + rightsize


def solve(tree, idx, n):
    if tree is None:
        return True
    if idx >= n:
        return False
    if tree.left and tree.left.data >= tree.data:
        return False
    if tree.right and tree.right.data >= tree.data:
        return False
    return (solve(tree.left, 2 * idx + 1, n)
            and solve(tree.right, 2 * idx + 2, n))


def isHeap(tree):
    if tree is None:
        return True
    n = size(tree)
    idx = 0
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
