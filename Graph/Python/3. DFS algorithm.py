# same function works for both directed and undirected graph
def dfsUtil(node, adj, visited, dfs):
    # Mark the node as visited
    visited[node] = True
    # Add the node to the DFS traversal
    dfs.append(node)
    # Explore all neighbors
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfsUtil(neighbor, adj, visited, dfs)


def dfsOfGraph(adj):
    # Number of vertices
    V = len(adj)
    # To store DFS traversal
    dfs = []
    # To track visited nodes
    visited = [False] * V
    if V:
        # Start DFS from node 0 (assuming graph is connected)
        dfsUtil(0, adj, visited, dfs)
    return dfs


def main():
    undirectedAdj = [[1, 2], [0, 3], [0, 4], [1, 5], [2, 5], [3, 4]]
    dfsUndirected = dfsOfGraph(undirectedAdj)
    print("DFS for Undirected Graph:", *dfsUndirected)
    directedAdj = [[1, 2], [3], [4], [5], [], []]
    dfsDirected = dfsOfGraph(directedAdj)
    print("DFS for Directed Graph:", *dfsDirected)


if __name__ == "__main__":
    main()


'''
Let V/E be vertex/edge counts.
Time: O(V + E): each visited vertex is processed once and each adjacency
entry is examined once (twice per undirected edge).
Space: O(V) auxiliary for visited and traversal stack/queue; supplied
adjacency storage is O(V + E).
Recursion depth is at most V. Only vertex 0's reachable component is
visited; dfs uses up to O(V) additional output space.
'''
