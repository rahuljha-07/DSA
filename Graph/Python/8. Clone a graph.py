from collections import deque


class Node:
    def __init__(self, _val=0, _neighbors=None):
        self.val = _val
        self.neighbors = list(_neighbors) if _neighbors is not None else []


# Function to clone the graph using BFS
def cloneGraph(node):
    if node is None:
        return None
    # Keeps track of cloned nodes
    map = {}
    # Clone the first node and add it to queue
    queue = deque([node])
    map[node] = Node(node.val)
    # BFS traversal
    while queue:
        current = queue.popleft()
        # Process all neighbors
        for neighbor in current.neighbors:
            if neighbor not in map:
                # Clone it
                map[neighbor] = Node(neighbor.val)
                # Add to queue for processing
                queue.append(neighbor)
            # Link the cloned node to its cloned neighbors
            map[current].neighbors.append(map[neighbor])
    # Return the cloned graph's entry point
    return map[node]


# Function to print a graph (for debugging)
def printGraph(node, visited):
    if node is None or visited.get(node, False):
        return
    # Mark node as visited
    visited[node] = True
    print(f"Node {node.val} -> {{ ", end="")
    for neighbor in node.neighbors:
        print(neighbor.val, end=" ")
    print("}")
    # Recursively print neighbors
    for neighbor in node.neighbors:
        printGraph(neighbor, visited)


class Solution:
    # Helper function to perform DFS and clone the graph
    def dfsClone(self, currentNode, clonedNodes):
        # Create a clone of the current node
        cloneNode = Node(currentNode.val)
        # Store the mapping of the current node to its clone
        clonedNodes[currentNode] = cloneNode
        # Traverse all the neighbors of the current node
        for neighbor in currentNode.neighbors:
            if neighbor in clonedNodes:
                cloneNode.neighbors.append(clonedNodes[neighbor])
            # If the neighbor is not yet cloned, clone it recursively and add it
            else:
                cloneNode.neighbors.append(self.dfsClone(neighbor, clonedNodes))
        # Return the clone of the current node
        return cloneNode

    def cloneGraph(self, node):
        # Handle the edge case where the graph is empty
        if node is None:
            return None
        # A map to keep track of visited nodes and their clones
        clonedNodes = {}
        # Start DFS from the given node
        return self.dfsClone(node, clonedNodes)


def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node3]
    node2.neighbors = [node1, node4, node3]
    node3.neighbors = [node1, node2, node4]
    node4.neighbors = [node2, node3]
    print("Original Graph:")
    visited = {}
    printGraph(node1, visited)
    clonedGraph = cloneGraph(node1)
    print("\nCloned Graph:")
    visitedCloned = {}
    printGraph(clonedGraph, visitedCloned)


if __name__ == "__main__":
    main()


'''
Let V/E be reachable vertex/edge counts.
Time: O(V + E) expected for BFS/DFS cloning: one clone per vertex, one
copied neighbor reference per adjacency entry; dictionary access averages O(1).
Space: O(V) auxiliary for mapping and queue/recursion, plus O(V + E)
output graph. Originals are not modified; object identity, not val,
is used as the mapping key, so repeated labels and cycles are supported.
'''
