from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Function to perform level-order traversal (Breadth-First Search) of a binary tree
def levelOrderTraversal(root):
    # Initialize an empty list to store the result
    result = []
    if root is None:
        return result
    # Start by pushing the root node into the queue
    nodeQueue = deque([root])
    # Process nodes in the queue while it's not empty
    while nodeQueue:
        # Get the front node in the queue
        currentNode = nodeQueue[0]
        # Add the current node's data to the result list
        result.append(currentNode.data)
        if currentNode.left:
            nodeQueue.append(currentNode.left)
        if currentNode.right:
            nodeQueue.append(currentNode.right)
        # Pop the processed node from the queue
        nodeQueue.popleft()
    # Return the final level-order traversal result
    return result


'''
Let n be the node count and w the maximum level width.
Time: O(n): every node enters/exits the queue once; deque operations
and result append are O(1) amortized.
Space: O(w) auxiliary for the BFS frontier, plus O(n) output values.
'''
