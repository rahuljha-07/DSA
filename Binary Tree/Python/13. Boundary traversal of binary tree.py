class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Function to collect the left boundary (excluding leaf nodes)
def getLeftBoundary(root, boundary):
    curr = root
    while curr:
        if curr.left or curr.right:
            boundary.append(curr.data)
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right


# Function to collect leaf nodes (in-order traversal)
def getLeafNodes(root, boundary):
    if not root:
        return
    # Traverse left subtree
    getLeafNodes(root.left, boundary)
    if not root.left and not root.right:
        boundary.append(root.data)
    # Traverse right subtree
    getLeafNodes(root.right, boundary)


# Function to collect the right boundary (excluding leaf nodes, in reverse order)
def getRightBoundary(root, boundary):
    # Temporary list to store right boundary
    temp = []
    curr = root
    while curr:
        if curr.left or curr.right:
            temp.append(curr.data)
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left
    # Add right boundary in reverse order
    for i in range(len(temp) - 1, -1, -1):
        boundary.append(temp[i])


def boundaryTraversal(root):
    boundary = []
    if not root:
        return boundary
    # Step 1: Add the root node
    boundary.append(root.data)
    if not root.left and not root.right:
        return boundary
    if root.left:
        getLeftBoundary(root.left, boundary)
    # Step 3: Collect all leaf nodes (in-order traversal)
    getLeafNodes(root, boundary)
    if root.right:
        getRightBoundary(root.right, boundary)
    return boundary


# Function to print the boundary traversal
def printBoundary(boundary):
    for val in boundary:
        print(val, end=" ")
    print()


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(8)
    root.left.right.right = Node(9)
    root.right.left = Node(6)
    root.right.right = Node(7)
    boundary = boundaryTraversal(root)
    printBoundary(boundary)


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n): collecting leaves scans the tree once; left/right boundaries
add at most O(h) each. A singleton root is emitted only once.
Space: O(h) auxiliary for leaf recursion and reversed right boundary,
plus O(b) output for b boundary nodes, at most O(n).
'''
