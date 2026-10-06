from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def zigZagTraversal(root):
    # To store the final zigzag order
    result = []
    # If the tree is empty, return an empty result
    if not root:
        return result
    # Push the root node into the queue
    nodeQueue = deque([root])
    # To alternate the traversal direction (even for left-to-right, odd for right-to-left)
    level = 0
    while nodeQueue:
        # Number of nodes at the current level
        levelSize = len(nodeQueue)
        # To store the nodes of the current level
        currentLevelNodes = []
        # Process all nodes at the current level
        while levelSize:
            currentNode = nodeQueue.popleft()
            # Add the node's data to the current level's list
            currentLevelNodes.append(currentNode.data)
            if currentNode.left:
                nodeQueue.append(currentNode.left)
            if currentNode.right:
                nodeQueue.append(currentNode.right)
            levelSize -= 1
        # If it's an even level, add nodes as they are
        if level % 2 == 0:
            for nodeData in currentLevelNodes:
                # Append the node's data to the result
                # Append the reversed node's data to the result
                result.append(nodeData)
        # If it's an odd level, reverse the nodes and add them to the result
        else:
            # Reverse the nodes
            currentLevelNodes.reverse()
            for nodeData in currentLevelNodes:
                result.append(nodeData)
        # Toggle the level to alternate the traversal direction
        level += 1
    # Return the final zigzag traversal result
    return result


'''
Let n be the node count and w maximum level width.
Time: O(n): BFS visits each node once; reversing alternating levels
touches at most n values altogether.
Space: O(w) auxiliary for the frontier/current level, plus O(n) output.
'''
