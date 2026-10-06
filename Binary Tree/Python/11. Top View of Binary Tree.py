from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Function to get the top view of a binary tree
def getTopView(root):
    # list to store the top view nodes
    topViewNodes = []
    # If the root is None, return an empty list
    if not root:
        return topViewNodes
    # Map to store the first node's data at each horizontal distance (HD)
    topViewMap = {}
    # Start with the root at horizontal distance 0
    nodeQueue = deque([(root, 0)])
    while nodeQueue:
        currentNode, horizontalDistance = nodeQueue.popleft()
        if horizontalDistance not in topViewMap:
            topViewMap[horizontalDistance] = currentNode.data
        if currentNode.left:
            nodeQueue.append((currentNode.left, horizontalDistance - 1))
        if currentNode.right:
            nodeQueue.append((currentNode.right, horizontalDistance + 1))
    # Traverse the map and add the nodes in order of HD to the result
    for entry in sorted(topViewMap):
        topViewNodes.append(topViewMap[entry])
    return topViewNodes


'''
Let n be the node count, d distinct horizontal distances, and w level width.
Time: O(n + d log d) expected: BFS with dictionary lookups is O(n);
sorting distances supplies the left-to-right order of C++ std::map.
Space: O(w + d) auxiliary for queue/map/sorted keys, plus O(d) output.
The first BFS value at each distance is retained.
'''
