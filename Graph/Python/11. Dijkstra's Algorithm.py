import heapq
import sys


# Function to initialize the graph as an adjacency list
def initializeGraph(n, m, tokens):
    # Create an adjacency list for the graph
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(next(tokens))
        v = int(next(tokens))
        wt = int(next(tokens))
        # Edge from `u` to `v` with weight `wt`
        # For undirected graph
        adj[u].append((v, wt))
        adj[v].append((u, wt))
    return adj


# Function to perform Dijkstra's algorithm and find the shortest paths
def dijkstra(n, source, adj):
    # Distance array to store shortest distance from the source
    # Initialize distances to infinity
    distTo = [float("inf")] * (n + 1)
    # Distance to the source is 0
    distTo[source] = 0
    # Push the source node into the priority queue
    pq = [(0, source)]
    # Implementing Dijkstra's algorithm
    while pq:
        currDist, currNode = heapq.heappop(pq)
        if currDist != distTo[currNode]:
            continue
        # Iterate over the neighbors of the current node
        for it in adj[currNode]:
            # Neighbor node
            nextNode = it[0]
            # Weight of the edge to the neighbor
            edgeWeight = it[1]
            # If a shorter path to the neighbor is found
            if distTo[nextNode] > currDist + edgeWeight:
                # Update the shortest distance
                distTo[nextNode] = currDist + edgeWeight
                # Push the updated distance and node
                heapq.heappush(pq, (distTo[nextNode], nextNode))
    return distTo


def main():
    tokens = iter(sys.stdin.read().split())
    n = int(next(tokens))
    m = int(next(tokens))
    adj = initializeGraph(n, m, tokens)
    source = int(next(tokens))
    distances = dijkstra(n, source, adj)
    print(f"The distances from source node {source} are:")
    print(*["INF" if distances[i] == float("inf") else distances[i]
            for i in range(1, n + 1)])


if __name__ == "__main__":
    main()


'''
Let V=n and E be undirected edge count; weights must be nonnegative.
Time: O(V + E log(E+1)): each finalized node scans its edges once;
successful relaxations push at most O(E) entries into a lazy binary heap.
Stale entries are skipped before scanning edges again. For simple graphs
this is commonly written O((V + E) log V).
Space: O(V + E) auxiliary for distances and heap, excluding input.
'''
