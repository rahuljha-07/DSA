from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def getBottomView(root):
    bottomViewNodes = []
    if not root:
        return bottomViewNodes
    bottomViewMap = {}
    nodeQueue = deque([(root, 0)])
    while nodeQueue:
        currentNode, horizontalDistance = nodeQueue.popleft()
        bottomViewMap[horizontalDistance] = currentNode.data
        if currentNode.left:
            nodeQueue.append((currentNode.left, horizontalDistance - 1))
        if currentNode.right:
            nodeQueue.append((currentNode.right, horizontalDistance + 1))
    for entry in sorted(bottomViewMap):
        bottomViewNodes.append(bottomViewMap[entry])
    return bottomViewNodes


'''
Let n be the node count, d distinct horizontal distances, and w level width.
Time: O(n + d log d) expected: BFS with dictionary lookups is O(n);
sorting distances supplies the left-to-right order of C++ std::map.
Space: O(w + d) auxiliary for queue/map/sorted keys, plus O(d) output.
Later BFS values overwrite earlier ones, retaining the bottom view.
'''
