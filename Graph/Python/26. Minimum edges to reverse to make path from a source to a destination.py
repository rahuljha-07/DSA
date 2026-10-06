import heapq


def minEdgesToReverse(n, edges, src, dest):
    # Step 1: Build the graph
    # Adjacency list
    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        u, v = edge
        # Add normal edge with weight 0
        graph[u].append((v, 0))
        # Add reversed edge with weight 1
        graph[v].append((u, 1))
    # Start from the source
    pq = [(0, src)]
    # Distance array
    dist = [float("inf")] * (n + 1)
    dist[src] = 0
    while pq:
        cost, node = heapq.heappop(pq)
        # If this cost is already greater, skip
        if cost > dist[node]:
            continue
        # Explore neighbors
        for neighbor, weight in graph[node]:
            if cost + weight < dist[neighbor]:
                dist[neighbor] = cost + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))
    # Step 3: Return the result
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
