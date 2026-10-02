class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


values = []
isBSTFlag = 1


def inOrderTraverse(root):
    global isBSTFlag
    if root is None or isBSTFlag == 0:
        return
    inOrderTraverse(root.left)
    if isBSTFlag == 0:
        return
    # Check the newly visited value too, including the final pair.
    if values and values[-1] >= root.data:
        isBSTFlag = 0
        return
    if len(values) < 2:
        values.append(root.data)
    else:
        values[0] = values[1]
        values[1] = root.data
    inOrderTraverse(root.right)


def isBST(root):
    global isBSTFlag
    isBSTFlag = 1
    values.clear()
    inOrderTraverse(root)
    return bool(isBSTFlag)


def insert(root, key):
    if not root:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)
    return root


def main():
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    print("The tree is a Binary Search Tree (BST)." if isBST(root)
          else "The tree is NOT a Binary Search Tree (BST).")


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n) worst case: inorder visits every node once and compares its
value with the previous one; invalid trees can exit earlier.
Space: O(h) auxiliary for recursion plus O(1) for at most two saved values.
Strictly increasing inorder values are required, so duplicates are rejected.
'''
