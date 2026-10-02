import heapq
import sys


def initializeGraph(n, m, tokens):
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(next(tokens))
        v = int(next(tokens))
        wt = int(next(tokens))
        adj[u].append((v, wt))
        adj[v].append((u, wt))
    return adj


def dijkstra(n, source, adj):
    distTo = [float("inf")] * (n + 1)
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
