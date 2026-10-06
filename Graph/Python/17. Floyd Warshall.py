import sys


# Floyd-Warshall Algorithm
def floydWarshall(n, graph):
    # Distance matrix
    dist = [row[:] for row in graph]
    # Perform the algorithm
    # Intermediate node
    for k in range(n):
        # Source node
        for i in range(n):
            # Destination node
            for j in range(n):
                # Update the distance between i and j via k
                if dist[i][k] != float("inf") and dist[k][j] != float("inf"):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    # Print the final distance matrix
    print("Shortest distances between every pair of vertices:")
    for i in range(n):
        for j in range(n):
            print("INF" if dist[i][j] == float("inf") else dist[i][j], end=" ")
        print()


def main():
    tokens = iter(sys.stdin.read().split())
    n = int(next(tokens))
    graph = [[float("inf")] * n for _ in range(n)]
    print("Enter the adjacency matrix (use INF for no direct edge):")
    for i in range(n):
        for j in range(n):
            input = next(tokens)
            graph[i][j] = float("inf") if input == "INF" else int(input)
    floydWarshall(n, graph)


if __name__ == "__main__":
    main()


'''
Let n be vertex count.
Time: O(n^3): three loops consider each intermediate/start/end combination;
copying and printing matrices add O(n^2), which does not dominate.
Space: O(n^2) auxiliary for a deep row-wise copy of graph; input stays
unchanged. Use zero diagonal distances and infinity for missing edges.
'''
