from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Function to get the bottom view of a binary tree
def getBottomView(root):
    # list to store the bottom view nodes
    bottomViewNodes = []
    # If the root is None, return an empty list
    if not root:
        return bottomViewNodes
    # Map to store the last node's data at each horizontal distance (HD)
    bottomViewMap = {}
    # Start with the root at horizontal distance 0
    nodeQueue = deque([(root, 0)])
    while nodeQueue:
        currentNode, horizontalDistance = nodeQueue.popleft()
        # Update the map with the current node's data at this HD
        # This ensures that the last node encountered at each HD is stored
        bottomViewMap[horizontalDistance] = currentNode.data
        if currentNode.left:
            nodeQueue.append((currentNode.left, horizontalDistance - 1))
        if currentNode.right:
            nodeQueue.append((currentNode.right, horizontalDistance + 1))
    # Traverse the map and add the nodes in order of HD to the result
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
