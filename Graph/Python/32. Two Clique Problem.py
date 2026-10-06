# Function to check if it's safe to color a node with a given color
def isSafe(node, color, graph, n, col):
    if graph[node][node]:
        # Adjacent node has the same color
        return False
    for k in range(n):
        if k != node and graph[k][node] == 1 and color[k] == col:
            return False
    return True


# Recursive function to solve the graph coloring problem
def solve(node, color, m, N, graph):
    if node == N:
        # Base case: all nodes are colored
        return True
    # Try assigning each color to the current node
    for i in range(1, m + 1):
        if isSafe(node, color, graph, N, i):
            # Assign color i to the node
            color[node] = i
            # Recur to the next node
            if solve(node + 1, color, m, N, graph):
                return True
            # Backtrack: Remove the assigned color
            color[node] = 0
    # If no color can be assigned, return false
    return False


# Function to determine if the graph can be colored with at most m colors
def graphColoring(graph, m, N):
    color = [0] * N
    if solve(0, color, m, N, graph):
        return True
    return False


# Function to create the complement of a graph
def complementGraph(graph, N):
    for i in range(N):
        for j in range(N):
            # Avoid self-loops
            if i != j:
                # Complement the edge
                graph[i][j] = not graph[i][j]


# Function to check if the complement of a graph is bipartite
def isComplementGraphBipartite(graph, N):
    # Step 1: Create the complement graph
    complementGraph(graph, N)
    # Step 2: Check if the complement graph is bipartite
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
