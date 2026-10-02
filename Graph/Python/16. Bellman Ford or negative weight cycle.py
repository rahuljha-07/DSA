import sys


def bellmanFord(n, edges, source, dist):
    dist[:] = [float("inf")] * n
    dist[source] = 0
    for count in range(1, n):
        for edge in edges:
            src, dest, weight = edge
            if dist[src] != float("inf") and dist[src] + weight < dist[dest]:
                dist[dest] = dist[src] + weight
    for edge in edges:
        src, dest, weight = edge
        if dist[src] != float("inf") and dist[src] + weight < dist[dest]:
            return False
    return True


def main():
    tokens = iter(sys.stdin.read().split())
    n = int(next(tokens))
    m = int(next(tokens))
    edges = [[int(next(tokens)) for _ in range(3)] for _ in range(m)]
    source = int(next(tokens))
    dist = []
    if bellmanFord(n, edges, source, dist):
        print(f"Shortest distances from source {source}:")
        print(*["INF" if d == float("inf") else d for d in dist])
    else:
        print("Graph contains a negative weight cycle.")


if __name__ == "__main__":
    main()


'''
Let V=n and E edge count.
Time: O(V*E + V): initialize V distances, then V-1 complete edge passes
and one extra pass to test for a reachable negative cycle.
Space: O(V) distance/output storage; O(1) additional loop state.
Only cycles reachable from source are detected. dist is replaced in place,
matching the C++ reference output; unreachable vertices retain infinity.
'''
