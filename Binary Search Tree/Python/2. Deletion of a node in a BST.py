class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Helper function to find the maximum value in the left subtree
def findMax(root):
    while root.right is not None:
        root = root.right
    return root


def deleteNode(root, key):
    # Base case: if the tree is empty, return None
    if root is None:
        return None
    # Traverse the tree to find the node to delete
    if key > root.data:
        # Search in the right subtree
        root.right = deleteNode(root.right, key)
    elif key < root.data:
        # Search in the left subtree
        root.left = deleteNode(root.left, key)
    else:
        if root.left is None and root.right is None:
            return None
        # Case 2: Node has only right child
        elif root.left is None:
            temp = root.right
            return temp
        # Case 3: Node has only left child
        elif root.right is None:
            temp = root.left
            return temp
        # Case 4: Node has two children
        else:
            maxNode = findMax(root.left)
            # Replace root's data with max value in left subtree
            root.data = maxNode.data
            root.left = deleteNode(root.left, maxNode.data)
    # Return the (possibly modified) root pointer
    return root


# Function to perform an in-order traversal for testing
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
