class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Helper function to perform in-order traversal and flatten the BST
def inorder(root, prev, head):
    # Base case: if the root is None, return
    if not root:
        return
    # Recursively traverse the left subtree
    inorder(root.left, prev, head)
    # If prev is not None, update the pointers to flatten the tree
    if prev[0]:
        prev[0].right = root
        prev[0].left = None
    else:
        head[0] = root
    prev[0] = root
    # Recursively traverse the right subtree
    inorder(root.right, prev, head)


# Function to flatten the BST into a sorted linked list
def flattenBST(root):
    # Initialize prev pointer as None
    prev = [None]
    # Initialize head pointer as None
    head = [None]
    # Perform in-order traversal to flatten the BST
    inorder(root, prev, head)
    if prev[0]:
        prev[0].left = None
    # Return the head of the flattened list
    return head[0]


# Helper function to print the linked list
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
