from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def diagonalTraversal(root):
    result = []
    if root is None:
        return result
    q = deque([root])
    while q:
        currentNode = q.popleft()
        while currentNode:
            result.append(currentNode.data)
            if currentNode.left:
                q.append(currentNode.left)
            currentNode = currentNode.right
    return result


def printDiagonalTraversal(root):
    result = diagonalTraversal(root)
    for val in result:
        print(val, end=" ")
    print()


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.right.left = Node(8)
    root.left.right.right = Node(9)
    printDiagonalTraversal(root)


if __name__ == "__main__":
    main()


'''
Let n be the node count.
Time: O(n): although loops are nested, each node belongs to one rightward
chain and is processed once; each left child is enqueued once.
Space: O(n) worst-case auxiliary for pending chains, plus O(n) result
values. Printing uses that same result list rather than copying it.
'''
