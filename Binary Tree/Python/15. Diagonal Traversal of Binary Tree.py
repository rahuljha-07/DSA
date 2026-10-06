from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Function to perform diagonal traversal of the binary tree
def diagonalTraversal(root):
    # list to store the result of the diagonal traversal
    result = []
    # If the tree is empty, return an empty result
    if root is None:
        return result
    # Start with the root node
    q = deque([root])
    while q:
        # Get the front node of the queue
        # Remove it from the queue
        currentNode = q.popleft()
        # Process all nodes in the current diagonal (i.e., all nodes that are reachable via
        # currentNode)
        while currentNode:
            # Add the current node's data to the result
            result.append(currentNode.data)
            if currentNode.left:
                q.append(currentNode.left)
            # Move to the right child for the same diagonal
            currentNode = currentNode.right
    # Return the diagonal traversal result
    return result


# Helper function to print the diagonal traversal
def printDiagonalTraversal(root):
    # Get the result from the diagonal traversal function
    result = diagonalTraversal(root)
    for val in result:
        print(val, end=" ")
    print()


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.right.left = Node(8)
    root.left.right.right = Node(9)
    printDiagonalTraversal(root)


if __name__ == "__main__":
    main()


'''
Let n be the node count.
Time: O(n): although loops are nested, each node belongs to one rightward
chain and is processed once; each left child is enqueued once.
Space: O(n) worst-case auxiliary for pending chains, plus O(n) result
values. Printing uses that same result list rather than copying it.
'''
