from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Function to get the left view of a binary tree
def getLeftView(root):
    # list to store the left view nodes
    leftViewNodes = []
    # If root is None, return an empty list
    if not root:
        return leftViewNodes
    nodeQueue = deque([root])
    while nodeQueue:
        # Number of nodes at the current level
        levelSize = len(nodeQueue)
        # The first node in each level is part of the left view
        leftViewNodes.append(nodeQueue[0].data)
        # Traverse all nodes at the current level
        while levelSize:
            currentNode = nodeQueue.popleft()
            if currentNode.left:
                nodeQueue.append(currentNode.left)
            if currentNode.right:
                nodeQueue.append(currentNode.right)
            levelSize -= 1
    return leftViewNodes


'''
Let n be the node count, h tree height, and w maximum level width.
Time: O(n): BFS visits each node once and records the first node per
level. Left-first enqueueing exposes the left view.
Space: O(w) auxiliary queue, plus O(h) output (one value per level).
'''
