class BSTInfo:
    def __init__(self, isBST, size, mini, maxi):
        self.isBST = isBST
        self.size = size
        self.mini = mini
        self.maxi = maxi


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def largestBSTSubtree(root):
    if not root:
        return BSTInfo(True, 0, float("inf"), float("-inf"))
    leftInfo = largestBSTSubtree(root.left)
    rightInfo = largestBSTSubtree(root.right)
    if (leftInfo.isBST and rightInfo.isBST
            and leftInfo.maxi < root.data and rightInfo.mini > root.data):
        return BSTInfo(True, leftInfo.size + rightInfo.size + 1,
                       min(root.data, leftInfo.mini),
                       max(root.data, rightInfo.maxi))
    else:
        return BSTInfo(False, max(leftInfo.size, rightInfo.size), -1, -1)


def largestBST(root):
    result = largestBSTSubtree(root)
    return result.size


def main():
    root1 = Node(1)
    root1.left = Node(4)
    root1.right = Node(4)
    root1.left.left = Node(6)
    root1.left.right = Node(8)
    print("Largest BST size in the first tree:", largestBST(root1))
    root2 = Node(6)
    root2.left = Node(6)
    root2.right = Node(2)
    root2.left.right = Node(2)
    root2.right.left = Node(1)
    root2.right.right = Node(3)
    print("Largest BST size in the second tree:", largestBST(root2))


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n): postorder visits each node once and combines two constant-size
BSTInfo results in O(1). Subtrees are not revalidated by full traversals.
Space: O(h) auxiliary for recursion and retained child results; each
result has only four fields. No O(n) result tree is allocated.
'''
