class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


# Global variables to store predecessor and successor
pre = None
suc = None


def findPreSuc(root, key):
    global pre, suc

    # Base case: stop if node is None
    if not root:
        return

    # Step 1: Traverse left subtree
    findPreSuc(root.left, key)

    # Step 2: Process current node
    if root.key < key:
        # Last smaller value found becomes predecessor
        pre = root
    elif root.key > key and suc is None:
        # First greater value found becomes successor
        suc = root

    # Step 3: Traverse right subtree
    findPreSuc(root.right, key)


# Insert a node into BST
def insert(root, key):
    if not root:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)

    return root


def main():
    global pre, suc

    # Create BST
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    key = 65

    # Reset predecessor and successor before searching
    pre = None
    suc = None

    # Find predecessor and successor
    findPreSuc(root, key)

    print(f"Predecessor is {pre.key}" if pre else "No Predecessor")
    print(f"Successor is {suc.key}" if suc else "No Successor")


if __name__ == "__main__":
    main()


"""
Time Complexity: O(n)
- We visit every node using inorder traversal.

Space Complexity: O(h)
- Recursive call stack depends on tree height.
- Balanced BST: O(log n)
- Skewed BST: O(n)

Inorder traversal: Left -> Root -> Right
BST inorder gives sorted values.

Predecessor = largest value smaller than key.
Successor = smallest value greater than key.
"""