from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def getLeftView(root):
    leftViewNodes = []
    if not root:
        return leftViewNodes
    nodeQueue = deque([root])
    while nodeQueue:
        levelSize = len(nodeQueue)
        leftViewNodes.append(nodeQueue[0].data)
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
