def topoSortUtil(node, adj, visited, topoStack):
    visited[node] = True
    for neighbor in adj[node]:
        if not visited[neighbor]:
            topoSortUtil(neighbor, adj, visited, topoStack)
    topoStack.append(node)


def topologicalSort(adj):
    V = len(adj)
    visited = [False] * V
    topoStack = []
    for i in range(V):
        if not visited[i]:
            topoSortUtil(i, adj, visited, topoStack)
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
