from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def getRightView(root):
    rightViewNodes = []
    if not root:
        return rightViewNodes
    nodeQueue = deque([root])
    while nodeQueue:
        levelSize = len(nodeQueue)
        rightViewNodes.append(nodeQueue[0].data)
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
