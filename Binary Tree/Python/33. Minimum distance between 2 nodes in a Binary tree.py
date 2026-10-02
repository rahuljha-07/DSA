class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def findLCA(root, n1, n2):
    if not root:
        return None
    if root.data == n1 or root.data == n2:
        return root
    leftLCA = findLCA(root.left, n1, n2)
    rightLCA = findLCA(root.right, n1, n2)
    if leftLCA and rightLCA:
        return root
    return leftLCA if leftLCA else rightLCA


def findDistanceFromRoot(root, target, distance):
    if not root:
        return -1
    if root.data == target:
        return distance
    leftDistance = findDistanceFromRoot(root.left, target, distance + 1)
    if leftDistance != -1:
        return leftDistance
    rightDistance = findDistanceFromRoot(root.right, target, distance + 1)
    if rightDistance != -1:
        return rightDistance
    return -1


def findMinDistance(root, a, b):
    lca = findLCA(root, a, b)
    if not lca:
        return -1
    distanceA = findDistanceFromRoot(lca, a, 0)
    distanceB = findDistanceFromRoot(lca, b, 0)
    if distanceA == -1 or distanceB == -1:
        return -1
    return distanceA + distanceB


def main():
    root = Node(11)
    root.left = Node(22)
    root.right = Node(33)
    root.left.left = Node(44)
    root.left.right = Node(55)
    root.right.left = Node(66)
    root.right.right = Node(77)
    a = 77
    b = 22
    minDistance = findMinDistance(root, a, b)
    print(f"Minimum distance between nodes {a} and {b} is {minDistance}")


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n): finding LCA and two target-distance searches each take at
most O(n). These are sequential passes, so their costs add, not multiply.
Space: O(h) auxiliary: only one recursive search stack is active at a time.
Distances count edges; an absent target returns -1 instead of a partial sum.
'''
