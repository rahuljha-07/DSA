# Perform topological sort using DFS
def topologicalSort(node, adj, visited, st):
    visited[node] = True
    for neighbor in adj[node]:
        if not visited[neighbor[0]]:
            topologicalSort(neighbor[0], adj, visited, st)
    st.append(node)


# Longest Path in a DAG using your approach
def findLongestPath(V, adj, source):
    # Step 1: Perform topological sort
    st = []
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            topologicalSort(i, adj, visited, st)
    # Step 2: Reverse the topological order
    topoOrder = []
    while st:
        topoOrder.append(st.pop())
    # Step 3: Initialize distances
    dist = [float("-inf")] * V
    dist[source] = 0
    # Step 4: BFS using topological order
    for u in topoOrder:
        # Process only reachable nodes
        if dist[u] != float("-inf"):
            for neighbor in adj[u]:
                v, weight = neighbor
                dist[v] = max(dist[v], dist[u] + weight)
    # Step 5: Output the longest distances
    print(f"Longest distances from source {source}:")
    for i in range(V):
        print(f"Node {i}: No path" if dist[i] == float("-inf")
              else f"Node {i}: {dist[i]}")


def main():
    V = 6
    adj = [[(1, 5), (2, 3)], [(3, 6), (2, 2)],
           [(4, 4), (5, 2), (3, 7)], [(5, 1)], [(5, 6)], []]
    source = 0
    findLongestPath(V, adj, source)


if __name__ == "__main__":
    main()


'''
Let V/E be vertex/edge counts.
Time: O(V + E): each visited vertex is processed once and each adjacency
entry is examined once (twice per undirected edge).
Space: O(V) auxiliary for visited and traversal stack/queue; supplied
adjacency storage is O(V + E).
DFS finishing order is followed by one relaxation per directed edge.
Distances and topological order each add O(V) storage. Input must be a DAG;
negative edge weights are allowed, with unreachable distances at -infinity.
'''
