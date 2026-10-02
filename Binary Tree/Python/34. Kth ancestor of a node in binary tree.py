class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


ancestor = -1


def findKthAncestor(root, node, K):
    global ancestor
    if root is None:
        return False
    if root.data == node:
        return True
    foundInLeft = findKthAncestor(root.left, node, K)
    foundInRight = findKthAncestor(root.right, node, K)
    if foundInLeft or foundInRight:
        K[0] -= 1
        if K[0] == 0:
            ancestor = root.data
            return False
        return True
    return False


def kthAncestor(root, node, K):
    global ancestor
    ancestor = -1
    findKthAncestor(root, node, [K])
    return ancestor


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    node = 5
    K = 2
    result = kthAncestor(root, node, K)
    if result == -1:
        print("No such ancestor exists.")
    else:
        print(f"The {K}th ancestor is: {result}")


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n): each node is processed once with O(1) work per visit.
Space: O(h) auxiliary for recursion: O(log n) on balanced trees and
O(n) on skewed trees. No new result tree is allocated.
K is decremented only while returning through ancestors of the target.
The one-item K holder preserves C++ reference semantics; the public
wrapper resets ancestor. Assumes unique keys and K >= 1.
'''
