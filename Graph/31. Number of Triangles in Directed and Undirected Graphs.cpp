#include <iostream>
using namespace std;

// Function to check if the graph is directed or undirected
bool isDirectedGraph(int graph[][4], int V) {
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            // In an undirected graph, graph[i][j] == graph[j][i]
            if (graph[i][j] != graph[j][i]) {
                return true; // Directed graph
            }
        }
    }
    return false; // Undirected graph
}

// Function to count the number of triangles in a graph
int countTriangles(int graph[][4], int V, bool isDirected) {
    int count_Triangle = 0;

    // Iterate through all possible triplets of vertices (i, j, k)
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            for (int k = 0; k < V; k++) {
                // Check if there is a triangle i -> j -> k -> i
                if (graph[i][j] && graph[j][k] && graph[k][i]) {
                    count_Triangle++;
                }
            }
        }
    }

    // Adjust the count based on whether the graph is directed or undirected
    if (isDirected) {
        count_Triangle /= 3; // Each triangle is counted 3 times
    } else {
        count_Triangle /= 6; // Each triangle is counted 6 times
    }

    return count_Triangle;
}

int main() {
    // Example graph (adjacency matrix)
    int V = 4;
    int graph[][4] = {
        {0, 1, 1, 0},
        {1, 0, 1, 1},
        {1, 1, 0, 1},
        {0, 1, 1, 0}
    };

    // Check if the graph is directed
    bool isDirected = isDirectedGraph(graph, V);

    // Count the number of triangles in the graph
    int totalTriangles = countTriangles(graph, V, isDirected);

    // Print the result
    cout << "The number of triangles in the graph is: " << totalTriangles << endl;

    return 0;
}
