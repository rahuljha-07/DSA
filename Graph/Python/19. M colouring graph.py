def isSafe(node, color, graph, n, col):
    if graph[node][node]:
        return False
    for k in range(n):
        if k != node and graph[k][node] == 1 and color[k] == col:
            return False
    return True


def solve(node, color, m, N, graph):
    if node == N:
        return True
    for i in range(1, m + 1):
        if isSafe(node, color, graph, N, i):
            color[node] = i
            if solve(node + 1, color, m, N, graph):
                return True
            color[node] = 0
    return False


def graphColoring(graph, m, N):
    color = [0] * N
    if solve(0, color, m, N, graph):
        return True
    return False


def main():
    N = 4
    m = 3
    graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
    print(f"Yes, the graph can be colored with {m} colors." if graphColoring(graph, m, N)
          else f"No, the graph cannot be colored with {m} colors.")


if __name__ == "__main__":
    main()


'''
Let N be vertex count and m available colors.
Time: O(N * sum(m^i, i=1..N)): up to m choices per node and an O(N)
matrix-row safety check per attempt. For m>=2 this is O(N*m^N);
for m=1 the bound is O(N^2).
Space: O(N) auxiliary colors and recursion; O(N^2) graph is supplied.
Undirected adjacency is assumed; self-loops cannot be properly colored.
'''
