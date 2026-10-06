from collections import deque


# function is same for both directed and unidrected graph
def bfsOfGraph(adj):
    # Number of vertices
    V = len(adj)
    # To store BFS traversal
    bfs = []
    # To track visited nodes
    visited = [False] * V
    q = deque()
    if V == 0:
        return bfs
    # Start BFS from node 0
    q.append(0)
    visited[0] = True
    while q:
        node = q.popleft()
        bfs.append(node)
        # Visit all unvisited neighbors
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
    return bfs


'''
Let V/E be vertex/edge counts.
Time: O(V + E): each visited vertex is processed once and each adjacency
entry is examined once (twice per undirected edge).
Space: O(V) auxiliary for visited and traversal stack/queue; supplied
adjacency storage is O(V + E).
Only the component reachable from vertex 0 is traversed, as in C++.
The returned traversal additionally occupies O(V) output space.
'''
