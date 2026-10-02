class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


def findPreSuc(root, pre, suc, key):
    if not root:
        return pre, suc
    pre, suc = findPreSuc(root.left, pre, suc, key)
    if root.key < key:
        pre = root
    elif root.key > key and not suc:
        suc = root
    pre, suc = findPreSuc(root.right, pre, suc, key)
    return pre, suc


def insert(root, key):
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root


def main():
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    key = 65
    pre = None
    suc = None
    pre, suc = findPreSuc(root, pre, suc, key)
    print(f"Predecessor is {pre.key}" if pre else "No Predecessor")
    print(f"Successor is {suc.key}" if suc else "No Successor")


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n): this implementation traverses the ENTIRE tree in order; it
does not prune BST branches to obtain an O(h) search.
Space: O(h) auxiliary for recursive calls. Returning pre/suc replaces
C++ reference parameters without allocating a list of all nodes.
'''
