from collections import deque


def dfsUtil(node, adj, visited, order):
    visited[node] = True
    order[node] = True
    for neighbor in adj[node]:
        if not visited[neighbor]:
            if dfsUtil(neighbor, adj, visited, order):
                return True
        elif order[neighbor]:
            return True
    order[node] = False
    return False


def isCyclic(adj):
    V = len(adj)
    visited = [False] * V
    order = [False] * V
    for i in range(V):
        if not visited[i]:
            if dfsUtil(i, adj, visited, order):
                return True
    return False


def hasCycleWithBFS(adj):
    V = len(adj)
    indegree = [0] * V
    for i in range(V):
        for neighbor in adj[i]:
            indegree[neighbor] += 1
    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)
    topoOrder = []
    count = 0
    while q:
        node = q.popleft()
        topoOrder.append(node)
        count += 1
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    if count != V:
        return True
    print("Topological Order:", *topoOrder)
    return False


def main():
    directedAdj = [[1, 2], [3], [3, 4], [], [5], [2]]
    print("The graph contains a cycle." if hasCycleWithBFS(directedAdj)
          else "The graph does not contain a cycle.")


if __name__ == "__main__":
    main()


'''
Let V/E be vertex/edge counts.
Time: O(V + E): each visited vertex is processed once and each adjacency
entry is examined once (twice per undirected edge).
Space: O(V) auxiliary for visited and traversal stack/queue; supplied
adjacency storage is O(V + E).
DFS distinguishes visited nodes from the current recursion path.
BFS counts indegrees and removes each edge once; fewer than V removals
means a cycle. topoOrder adds O(V) storage but not a higher space bound.
'''
