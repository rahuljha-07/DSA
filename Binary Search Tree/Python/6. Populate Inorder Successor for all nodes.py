class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.next = None


prevNode = None


def populateInorderSuccessor(currentNode):
    global prevNode
    if not currentNode:
        return
    populateInorderSuccessor(currentNode.left)
    if prevNode is not None:
        prevNode.next = currentNode
    prevNode = currentNode
    populateInorderSuccessor(currentNode.right)


def insert(root, key):
    if not root:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)
    return root


def printInorderSuccessors(root):
    if root:
        printInorderSuccessors(root.left)
        if root.next:
            print(f"In-order successor of {root.data} is {root.next.data}")
        else:
            print(f"In-order successor of {root.data} is NULL")
        printInorderSuccessors(root.right)


def main():
    global prevNode
    root = None
    root = insert(root, 4)
    insert(root, 2)
    insert(root, 5)
    insert(root, 1)
    insert(root, 3)
    prevNode = None
    populateInorderSuccessor(root)
    printInorderSuccessors(root)


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n): inorder visits each node once and writes each successor link
in O(1). Printing all successors is another O(n) pass.
Space: O(h) auxiliary for recursion, plus one global prevNode pointer.
As in the source, reset prevNode to None before processing a separate tree.
The maximum node's next should initially be None.
'''
