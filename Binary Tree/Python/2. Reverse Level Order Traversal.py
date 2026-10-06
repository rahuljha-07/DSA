from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Function to perform Reverse Level Order Traversal
def reverseLevelOrderTraversal(root):
    # To store the final result of reverse level-order traversal
    result = []
    # If the tree is empty, return an empty result
    if not root:
        return result
    # Start with the root node
    nodeQueue = deque([root])
    # Process nodes level by level
    while nodeQueue:
        # Get the node at the front of the queue
        # Remove the node from the queue
        currentNode = nodeQueue.popleft()
        # Add current node's data to the result
        result.append(currentNode.data)
        if currentNode.right:
            nodeQueue.append(currentNode.right)
        if currentNode.left:
            nodeQueue.append(currentNode.left)
    # Reverse the result list to get reverse level-order traversal
    result.reverse()
    # Return the reversed level-order traversal result
    return result


'''
Let n be the node count and w the maximum level width.
Time: O(n): BFS visits each node once; reversing n result values adds
one more O(n) pass. Right-first enqueueing preserves left-to-right order
after reversal. Space: O(w) auxiliary queue, plus O(n) output values.
'''
