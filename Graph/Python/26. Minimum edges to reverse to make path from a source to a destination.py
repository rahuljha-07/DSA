import heapq


def minEdgesToReverse(n, edges, src, dest):
    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        u, v = edge
        graph[u].append((v, 0))
        graph[v].append((u, 1))
    pq = [(0, src)]
    dist = [float("inf")] * (n + 1)
    dist[src] = 0
    while pq:
        cost, node = heapq.heappop(pq)
        if cost > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            if cost + weight < dist[neighbor]:
                dist[neighbor] = cost + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))
    return -1 if dist[dest] == float("inf") else dist[dest]


def main():
    n = 6
    edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)]
    src = 1
    dest = 5
    result = minEdgesToReverse(n, edges, src, dest)
    print("Destination not reachable." if result == -1
          else f"Minimum edges to reverse: {result}")


if __name__ == "__main__":
    main()


'''
Let n be vertices and E original directed edges.
Time: O(n + E log(E+1)): create 2E weighted edges, then Dijkstra processes
O(E) relaxations with a lazy heap; stale entries skip repeat edge scans.
Space: O(n + E) auxiliary graph, distances, and heap.
Original direction costs 0, reversing costs 1; the source's heap approach
is retained rather than replaced with 0-1 BFS.
'''
