class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def findMax(root):
    while root.right is not None:
        root = root.right
    return root


def deleteNode(root, key):
    if root is None:
        return None
    if key > root.data:
        root.right = deleteNode(root.right, key)
    elif key < root.data:
        root.left = deleteNode(root.left, key)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            temp = root.right
            return temp
        elif root.right is None:
            temp = root.left
            return temp
        else:
            maxNode = findMax(root.left)
            root.data = maxNode.data
            root.left = deleteNode(root.left, maxNode.data)
    return root


def inOrderTraversal(root):
    if not root:
        return
    inOrderTraversal(root.left)
    print(root.data, end=" ")
    inOrderTraversal(root.right)


def main():
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)
    keyToDelete = 3
    root = deleteNode(root, keyToDelete)
    print("In-order traversal after deletion: ", end="")
    inOrderTraversal(root)
    print()


if __name__ == "__main__":
    main()


'''
Let h be tree height and n its node count.
Time: O(h): locating the key, finding its predecessor, and deleting that
predecessor follow paths whose total length is O(h).
Space: O(h) auxiliary for recursion; existing nodes are relinked.
Balanced trees use O(log n); skewed trees can use O(n).
'''
