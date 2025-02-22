#include <vector>
#include <iostream>
using namespace std;

// Helper function to perform DFS traversal
void dfsUtil(int node, vector<vector<int>>& adj, vector<bool>& visited) {
    visited[node] = true; // Mark the current node as visited
    
    // Visit all neighbors of the current node
    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            dfsUtil(neighbor, adj, visited);
        }
    }
}

// Function to count connected components and determine redundancy
int makeConnected(int n, vector<vector<int>>& connections) {
    if (connections.size() < n - 1) return -1; // Not enough connections to connect all nodes

    // Build adjacency list
    vector<vector<int>> adj(n);
    for (const auto& conn : connections) {
        adj[conn[0]].push_back(conn[1]);
        adj[conn[1]].push_back(conn[0]);
    }

    // Count connected components using DFS
    vector<bool> visited(n, false);
    int components = 0;

    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            components++;
            dfsUtil(i, adj, visited); // Perform DFS from this node
        }
    }

    // Calculate redundant connections
    int redundantEdges = connections.size() - ((n - 1) - (components - 1));
    return (redundantEdges >= components - 1) ? components - 1 : -1;
}

int main() {
    int n1 = 4;
    vector<vector<int>> connections1 = {{0, 1}, {0, 2}, {1, 2}};
    cout << "Output: " << makeConnected(n1, connections1) << endl; // Output: 1

    int n2 = 6;
    vector<vector<int>> connections2 = {{0, 1}, {0, 2}, {0, 3}, {1, 2}, {1, 3}};
    cout << "Output: " << makeConnected(n2, connections2) << endl; // Output: 2

    int n3 = 6;
    vector<vector<int>> connections3 = {{0, 1}, {0, 2}, {0, 3}, {1, 2}};
    cout << "Output: " << makeConnected(n3, connections3) << endl; // Output: -1

    return 0;
}
