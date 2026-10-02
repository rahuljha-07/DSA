from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def zigZagTraversal(root):
    result = []
    if not root:
        return result
    nodeQueue = deque([root])
    level = 0
    while nodeQueue:
        levelSize = len(nodeQueue)
        currentLevelNodes = []
        while levelSize:
            currentNode = nodeQueue.popleft()
            currentLevelNodes.append(currentNode.data)
            if currentNode.left:
                nodeQueue.append(currentNode.left)
            if currentNode.right:
                nodeQueue.append(currentNode.right)
            levelSize -= 1
        if level % 2 == 0:
            for nodeData in currentLevelNodes:
                result.append(nodeData)
        else:
            currentLevelNodes.reverse()
            for nodeData in currentLevelNodes:
                result.append(nodeData)
        level += 1
    return result


'''
Let n be the node count and w maximum level width.
Time: O(n): BFS visits each node once; reversing alternating levels
touches at most n values altogether.
Space: O(w) auxiliary for the frontier/current level, plus O(n) output.
'''
