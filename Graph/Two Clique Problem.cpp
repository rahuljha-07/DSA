#include <iostream>
using namespace std;

// Function to check if it's safe to color a node with a given color
bool isSafe(int node, int color[], bool graph[101][101], int n, int col) {
    for (int k = 0; k < n; k++) {
        if (graph[node][k] && color[k] == col) {
            return false; // Adjacent node has the same color
        }
    }
    return true;
}

// Recursive function to solve the graph coloring problem
bool solve(int node, int color[], int m, int N, bool graph[101][101]) {
    if (node == N) {
        return true; // Base case: all nodes are colored
    }

    // Try assigning each color to the current node
    for (int i = 1; i <= m; i++) {
        if (isSafe(node, color, graph, N, i)) {
            color[node] = i; // Assign color i to the node

            // Recur to the next node
            if (solve(node + 1, color, m, N, graph)) {
                return true;
            }

            // Backtrack: Remove the assigned color
            color[node] = 0;
        }
    }

    return false; // If no color can be assigned, return false
}

// Function to determine if the graph can be colored with at most m colors
bool graphColoring(bool graph[101][101], int m, int N) {
    int color[N] = {0}; // Array to store colors assigned to nodes
    return solve(0, color, m, N, graph);
}

// Function to create the complement of a graph
void complementGraph(bool graph[101][101], int N) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i != j) { // Avoid self-loops
                graph[i][j] = !graph[i][j]; // Complement the edge
            }
        }
    }
}

// Function to check if the complement of a graph is bipartite
bool isComplementGraphBipartite(bool graph[101][101], int N) {
    // Step 1: Create the complement graph
    complementGraph(graph, N);

    // Step 2: Check if the complement graph is bipartite
    return graphColoring(graph, 2, N);
}

int main() {
    int N = 4; // Number of vertices
    bool graph[101][101] = {
        {0, 1, 1, 0},
        {1, 0, 0, 1},
        {1, 0, 0, 1},
        {0, 1, 1, 0}
    };

    // Check if the complement graph is bipartite
    if (isComplementGraphBipartite(graph, N)) {
        cout << "Yes, the complement graph is bipartite (2-colorable)." << endl;
    } else {
        cout << "No, the complement graph is not bipartite." << endl;
    }

    return 0;
}
