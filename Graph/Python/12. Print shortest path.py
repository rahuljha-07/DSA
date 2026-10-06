import heapq
import sys


# Function to initialize the graph as an adjacency list
def initializeGraph(n, m, tokens):
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(next(tokens))
        v = int(next(tokens))
        wt = int(next(tokens))
        # For undirected graph
        adj[u].append((v, wt))
        adj[v].append((u, wt))
    return adj


# Dijkstra's algorithm to find the shortest paths from the source
def dijkstra(n, source, adj):
    distTo = [float("inf")] * (n + 1)
    parent = [-1] * (n + 1)
    parent[source] = source
    distTo[source] = 0
    pq = [(0, source)]
    while pq:
        currDist, currNode = heapq.heappop(pq)
        if currDist != distTo[currNode]:
            continue
        for it in adj[currNode]:
            nextNode = it[0]
            edgeWeight = it[1]
            if distTo[nextNode] > currDist + edgeWeight:
                distTo[nextNode] = currDist + edgeWeight
                parent[nextNode] = currNode
                heapq.heappush(pq, (distTo[nextNode], nextNode))
    return distTo, parent


# Function to get the shortest path from source to a destination using the parent array
def getPath(destination, parent):
    if parent[destination] == -1:
        # Destination is unreachable
        return [-1]
    path = []
    node = destination
    while parent[node] != node:
        path.append(node)
        node = parent[node]
    path.append(node)
    path.reverse()
    return path


def main():
    tokens = iter(sys.stdin.read().split())
    n = int(next(tokens))
    m = int(next(tokens))
    adj = initializeGraph(n, m, tokens)
    source = int(next(tokens))
    distances, parents = dijkstra(n, source, adj)
    print(f"The distances from source node {source} are:")
    print(*["INF" if distances[i] == float("inf") else distances[i]
            for i in range(1, n + 1)])
    print(f"Shortest paths from source node {source} to all nodes:")
    for i in range(1, n + 1):
        if distances[i] != float("inf"):
            path = getPath(i, parents)
            print(f"Path to node {i}:", *path)
        else:
            print(f"Node {i} is unreachable from the source.")


if __name__ == "__main__":
    main()


'''
Let V=n and E be undirected edge count; weights must be nonnegative.
Time: O(V + E log(E+1)): each finalized node scans its edges once;
successful relaxations push at most O(E) entries into a lazy binary heap.
Stale entries are skipped before scanning edges again. For simple graphs
this is commonly written O((V + E) log V).
Space: O(V + E) auxiliary for distances/parents and heap, excluding input.
One getPath costs O(V) time/output worst case; printing paths to ALL V
nodes can add O(V^2) work, beyond the shortest-distance computation.
'''
