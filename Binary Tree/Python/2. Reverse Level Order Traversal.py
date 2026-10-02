from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def reverseLevelOrderTraversal(root):
    result = []
    if not root:
        return result
    nodeQueue = deque([root])
    while nodeQueue:
        currentNode = nodeQueue.popleft()
        result.append(currentNode.data)
        if currentNode.right:
            nodeQueue.append(currentNode.right)
        if currentNode.left:
            nodeQueue.append(currentNode.left)
    result.reverse()
    return result


'''
Let n be the node count and w the maximum level width.
Time: O(n): BFS visits each node once; reversing n result values adds
one more O(n) pass. Right-first enqueueing preserves left-to-right order
after reversal. Space: O(w) auxiliary queue, plus O(n) output values.
'''
