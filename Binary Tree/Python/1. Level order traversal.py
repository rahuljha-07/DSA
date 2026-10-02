from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def levelOrderTraversal(root):
    result = []
    if root is None:
        return result
    nodeQueue = deque([root])
    while nodeQueue:
        currentNode = nodeQueue[0]
        result.append(currentNode.data)
        if currentNode.left:
            nodeQueue.append(currentNode.left)
        if currentNode.right:
            nodeQueue.append(currentNode.right)
        nodeQueue.popleft()
    return result


'''
Let n be the node count and w the maximum level width.
Time: O(n): every node enters/exits the queue once; deque operations
and result append are O(1) amortized.
Space: O(w) auxiliary for the BFS frontier, plus O(n) output values.
'''
