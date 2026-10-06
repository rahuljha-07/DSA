from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Function to get the right view of a binary tree
def getRightView(root):
    # list to store the right view nodes
    rightViewNodes = []
    # If root is None, return an empty list
    if not root:
        return rightViewNodes
    nodeQueue = deque([root])
    while nodeQueue:
        # Number of nodes at the current level
        levelSize = len(nodeQueue)
        # The first node in each level is part of the right view
        rightViewNodes.append(nodeQueue[0].data)
        # Traverse all nodes at the current level
        while levelSize:
            currentNode = nodeQueue.popleft()
            if currentNode.right:
                nodeQueue.append(currentNode.right)
            if currentNode.left:
                nodeQueue.append(currentNode.left)
            levelSize -= 1
    return rightViewNodes


'''
Let n be the node count, h tree height, and w maximum level width.
Time: O(n): BFS visits each node once and records the first node per
level. Right-first enqueueing exposes the right view.
Space: O(w) auxiliary queue, plus O(h) output (one value per level).
'''
