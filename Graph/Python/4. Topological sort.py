# Helper function to perform DFS and store nodes in topological order
def topoSortUtil(node, adj, visited, topoStack):
    # Mark the node as visited
    visited[node] = True
    # Explore all neighbors
    for neighbor in adj[node]:
        if not visited[neighbor]:
            topoSortUtil(neighbor, adj, visited, topoStack)
    # Push the node into the stack after exploring all its neighbors
    topoStack.append(node)


def topologicalSort(adj):
    # Number of vertices
    V = len(adj)
    # To track visited nodes
    visited = [False] * V
    # Stack to store topological order
    topoStack = []
    # Perform DFS for all unvisited nodes
    for i in range(V):
        if not visited[i]:
            topoSortUtil(i, adj, visited, topoStack)
    # Extract nodes from the stack to get the topological order
    topoOrder = []
    while topoStack:
        topoOrder.append(topoStack.pop())
    return topoOrder


def main():
    directedAdj = [[1, 2], [3], [3, 4], [], [5], []]
    topoOrder = topologicalSort(directedAdj)
    print("Topological Sort for Directed Graph:", *topoOrder)


if __name__ == "__main__":
    main()


'''
Let V/E be vertex/edge counts.
Time: O(V + E): each visited vertex is processed once and each adjacency
entry is examined once (twice per undirected edge).
Space: O(V) auxiliary for visited and traversal stack/queue; supplied
adjacency storage is O(V + E).
Reverse DFS finishing order needs O(V) stack/output values.
Input must be a DAG: this source approach does not detect directed cycles.
'''
