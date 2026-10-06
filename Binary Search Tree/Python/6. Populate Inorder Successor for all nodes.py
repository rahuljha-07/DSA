class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.next = None


prevNode = None


# Function to populate the next pointer (in-order successor) for all nodes
def populateInorderSuccessor(currentNode):
    global prevNode
    # Base case: If current node is None, return
    if not currentNode:
        return
    # Traverse the left subtree first (in-order)
    populateInorderSuccessor(currentNode.left)
    # If prevNode is not None, set the next pointer of prevNode to currentNode
    if prevNode is not None:
        prevNode.next = currentNode
    # Update prevNode to current node
    prevNode = currentNode
    # Traverse the right subtree
    populateInorderSuccessor(currentNode.right)


# Helper function to insert nodes into the binary search tree
def insert(root, key):
    # If the tree is empty, create a new node
    if not root:
        return Node(key)
    if key < root.data:
        # Insert into the left subtree
        root.left = insert(root.left, key)
    elif key > root.data:
        # Insert into the right subtree
        root.right = insert(root.right, key)
    return root


# Helper function to print the in-order successor of each node
def printInorderSuccessors(root):
    if root:
        # Print the left subtree first
        printInorderSuccessors(root.left)
        if root.next:
            print(f"In-order successor of {root.data} is {root.next.data}")
        else:
            print(f"In-order successor of {root.data} is NULL")
        # Print the right subtree
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
