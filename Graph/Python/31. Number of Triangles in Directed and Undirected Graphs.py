# Function to check if the graph is directed or undirected
def isDirectedGraph(graph, V):
    for i in range(V):
        for j in range(V):
            # In an undirected graph, graph[i][j] == graph[j][i]
            if graph[i][j] != graph[j][i]:
                # Directed graph
                return True
    # Undirected graph
    return False


# Function to count the number of triangles in a graph
def countTriangles(graph, V, isDirected):
    count_Triangle = 0
    # Iterate through all possible triplets of vertices (i, j, k)
    for i in range(V):
        for j in range(V):
            for k in range(V):
                if graph[i][j] and graph[j][k] and graph[k][i]:
                    count_Triangle += 1
    # Adjust the count based on whether the graph is directed or undirected
    if isDirected:
        # Each triangle is counted 3 times
        count_Triangle //= 3
    else:
        # Each triangle is counted 6 times
        count_Triangle //= 6
    return count_Triangle


def main():
    V = 4
    graph = [[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]]
    isDirected = isDirectedGraph(graph, V)
    totalTriangles = countTriangles(graph, V, isDirected)
    print("The number of triangles in the graph is:", totalTriangles)


if __name__ == "__main__":
    main()


'''
Let V be vertex count.
Time: O(V^3): examine every ordered triple; the symmetry check adds O(V^2).
Space: O(1) auxiliary besides the supplied O(V^2) matrix.
Divide by 3 for directed cyclic triangles or 6 for undirected triangles.
Assumes no self-loops. A symmetric matrix can also represent a directed
graph with reciprocal arcs: symmetry alone cannot infer its intended type;
pass the correct isDirected flag when that distinction matters.
'''
