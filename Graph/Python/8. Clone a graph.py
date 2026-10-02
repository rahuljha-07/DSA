from collections import deque


class Node:
    def __init__(self, _val=0, _neighbors=None):
        self.val = _val
        self.neighbors = list(_neighbors) if _neighbors is not None else []


def cloneGraph(node):
    if node is None:
        return None
    map = {}
    queue = deque([node])
    map[node] = Node(node.val)
    while queue:
        current = queue.popleft()
        for neighbor in current.neighbors:
            if neighbor not in map:
                map[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            map[current].neighbors.append(map[neighbor])
    return map[node]


def printGraph(node, visited):
    if node is None or visited.get(node, False):
        return
    visited[node] = True
    print(f"Node {node.val} -> {{ ", end="")
    for neighbor in node.neighbors:
        print(neighbor.val, end=" ")
    print("}")
    for neighbor in node.neighbors:
        printGraph(neighbor, visited)


class Solution:
    def dfsClone(self, currentNode, clonedNodes):
        cloneNode = Node(currentNode.val)
        clonedNodes[currentNode] = cloneNode
        for neighbor in currentNode.neighbors:
            if neighbor in clonedNodes:
                cloneNode.neighbors.append(clonedNodes[neighbor])
            else:
                cloneNode.neighbors.append(self.dfsClone(neighbor, clonedNodes))
        return cloneNode

    def cloneGraph(self, node):
        if node is None:
            return None
        clonedNodes = {}
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
