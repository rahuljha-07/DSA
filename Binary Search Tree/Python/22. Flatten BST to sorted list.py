class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def inorder(root, prev, head):
    if not root:
        return
    inorder(root.left, prev, head)
    if prev[0]:
        prev[0].right = root
        prev[0].left = None
    else:
        head[0] = root
    prev[0] = root
    inorder(root.right, prev, head)


def flattenBST(root):
    prev = [None]
    head = [None]
    inorder(root, prev, head)
    if prev[0]:
        prev[0].left = None
    return head[0]


def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.right
    print()


def main():
    root = Node(5)
    root.left = Node(3)
    root.right = Node(8)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(9)
    flattenedHead = flattenBST(root)
    printList(flattenedHead)


if __name__ == "__main__":
    main()


'''
Let n be the node count and h the original tree height.
Time: O(n): inorder visits each node once and rewires a constant number
of links. The final node's left link is cleared too.
Space: O(h) auxiliary for recursion, plus two one-item reference holders.
Output nodes are reused; the sorted chain is traversed through right.
'''
