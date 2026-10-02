from collections import deque


def dfsCycleUtil(node, parent, adj, visited):
    visited[node] = True
    for neighbor in adj[node]:
        if not visited[neighbor]:
            if dfsCycleUtil(neighbor, node, adj, visited):
                return True
        elif neighbor != parent:
            return True
    return False


def dfsCycleDetection(V, adj):
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            if dfsCycleUtil(i, -1, adj, visited):
                return True
    return False


def bfsCycleDetection(V, adj):
    visited = [False] * V
    q = deque()
    for i in range(V):
        if not visited[i]:
            q.append((i, -1))
            visited[i] = True
            while q:
                node, parent = q.popleft()
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append((neighbor, node))
                    elif neighbor != parent:
                        return True
    return False


'''
Let V/E be vertex/edge counts.
Time: O(V + E): each visited vertex is processed once and each adjacency
entry is examined once (twice per undirected edge).
Space: O(V) auxiliary for visited and traversal stack/queue; supplied
adjacency storage is O(V + E).
Both variants inspect all components. DFS tracks a parent in recursion;
BFS stores (node, parent) pairs. Assumes a simple undirected graph.
'''
