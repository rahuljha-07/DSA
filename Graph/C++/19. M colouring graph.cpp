#include <iostream>
#include <vector>
using namespace std;

// Function to check if it's safe to color a node with a given color
bool isSafe(int node, vector<int> &color, bool graph[101][101], int n, int col) {
    for (int k = 0; k < n; k++) {
        if (k != node && graph[k][node] == 1 && color[k] == col) {
            return false; // Adjacent node has the same color
        }
    }
    return true;
}

// Recursive function to solve the graph coloring problem
bool solve(int node, vector<int> &color, int m, int N, bool graph[101][101]) {
    // Base case: If all nodes are colored, return true
    if (node == N) {
        return true;
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
    vector<int> color(N, 0); // Array to store colors assigned to nodes

    // Solve the coloring problem starting from node 0
    if (solve(0, color, m, N, graph)) {
        return true;
    }

    return false; // If no solution exists
}

int main() {
    int N = 4; // Number of vertices
    int m = 3; // Number of colors
    bool graph[101][101] = {
        {0, 1, 1, 1},
        {1, 0, 1, 0},
        {1, 1, 0, 1},
        {1, 0, 1, 0}
    };

    if (graphColoring(graph, m, N)) {
        cout << "Yes, the graph can be colored with " << m << " colors." << endl;
    } else {
        cout << "No, the graph cannot be colored with " << m << " colors." << endl;
    }

    return 0;
}
