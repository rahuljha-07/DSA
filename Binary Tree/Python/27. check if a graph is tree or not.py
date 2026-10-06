# Function to perform DFS and check for cycles
def hasCycle(node, parent, adjList, visited):
    # Mark the current node as visited
    visited[node] = True
    # Visit all adjacent nodes
    for neighbor in adjList[node]:
        if not visited[neighbor]:
            # Recur for unvisited neighbors
            if hasCycle(neighbor, node, adjList, visited):
                # If an adjacent node is visited and not the parent of the current node,
                # there's a cycle
                return True
        elif neighbor != parent:
            return True
    return False


# Function to check if a graph is a tree
def isTree(V, edges):
    # A tree must have exactly V-1 edges
    if V <= 0 or len(edges) != V - 1:
        return False
    # Create an adjacency list for the graph
    adjList = [[] for _ in range(V)]
    for edge in edges:
        adjList[edge[0]].append(edge[1])
        adjList[edge[1]].append(edge[0])
    # Visited array to mark visited nodes
    visited = [False] * V
    # Check for cycle starting from node 0
    if hasCycle(0, -1, adjList, visited):
        return False
    # Check if all nodes are visited (ensuring the graph is connected)
    for i in range(V):
        if not visited[i]:
            return False
    # If no cycles and the graph is connected, it's a tree
    return True


def main():
    V = 5
    edges = [(0, 1), (0, 2), (1, 3), (1, 4)]
    print("The graph is a tree." if isTree(V, edges)
          else "The graph is not a tree.")


if __name__ == "__main__":
    main()


'''
Let V be vertex count and E edge count.
Time: O(V + E): build adjacency lists and run DFS once, inspecting each
undirected edge at most twice, then scan visited. Edge-count mismatch
returns immediately; a tree candidate has E = V - 1, so its work is O(V).
Space: O(V + E) auxiliary for adjacency/visited and up to O(V) DFS depth.
Input is an undirected graph with vertex labels 0..V-1.
'''
