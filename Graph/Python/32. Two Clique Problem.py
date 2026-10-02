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


def complementGraph(graph, N):
    for i in range(N):
        for j in range(N):
            if i != j:
                graph[i][j] = not graph[i][j]


def isComplementGraphBipartite(graph, N):
    complementGraph(graph, N)
    return graphColoring(graph, 2, N)


def main():
    N = 4
    graph = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
    print("Yes, the complement graph is bipartite (2-colorable)."
          if isComplementGraphBipartite(graph, N)
          else "No, the complement graph is not bipartite.")


if __name__ == "__main__":
    main()


'''
Let N be vertex count.
Time: O(N^2 + N*2^N): complementing scans N^2 entries, then retained
backtracking tries up to 2^N colorings with O(N) safety checks per attempt.
This is not replaced with a linear-time bipartite BFS.
Space: O(N) auxiliary colors/recursion, excluding supplied O(N^2) matrix.
The matrix is complemented IN PLACE; assumes a simple undirected graph.
'''
