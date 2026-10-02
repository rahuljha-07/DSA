#include <bits/stdc++.h>
using namespace std;

// Floyd-Warshall Algorithm
void floydWarshall(int n, vector<vector<int>>& graph) {
    vector<vector<int>> dist = graph; // Distance matrix

    // Perform the algorithm
    for (int k = 0; k < n; ++k) {        // Intermediate node
        for (int i = 0; i < n; ++i) {    // Source node
            for (int j = 0; j < n; ++j) {// Destination node
                // Update the distance between i and j via k
                if (dist[i][k] != INT_MAX && dist[k][j] != INT_MAX) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }

    // Print the final distance matrix
    cout << "Shortest distances between every pair of vertices:\n";
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (dist[i][j] == INT_MAX) {
                cout << "INF ";
            } else {
                cout << dist[i][j] << " ";
            }
        }
        cout << endl;
    }
}

int main() {
    int n; // Number of vertices
    cin >> n;

    vector<vector<int>> graph(n, vector<int>(n, INT_MAX)); // Graph adjacency matrix

    // Input the graph
    cout << "Enter the adjacency matrix (use INF for no direct edge):\n";
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            string input;
            cin >> input;
            if (input == "INF") {
                graph[i][j] = INT_MAX;
            } else {
                graph[i][j] = stoi(input);
            }
        }
    }

    // Perform Floyd-Warshall
    floydWarshall(n, graph);

    return 0;
}
