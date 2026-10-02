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
    
    int totalEdges = connections.size(); // Total number of existing cables

    int minEdgesNeeded = n - 1; // We need at least (n - 1) cables to connect all computers

    // connections.size() - (n - 1)
    //This gives you how many extra (redundant) wires you have — ones forming cycles. These are free to move.
    
    // Counted earlier: 'components' = number of separate groups (disconnected parts)
    // To connect all components into one group, we need (components - 1) connections (bridges)
    int neededBridges = components - 1;

    // Any cables beyond the minimum are extra, meaning they form cycles and can be reused elsewhere
    int extraEdges = totalEdges - minEdgesNeeded;

    // If we have enough extra cables to connect the groups, return how many bridges we need
    // Otherwise, return -1 because we can't connect everything
    return (extraEdges >= neededBridges) ? neededBridges : -1;
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
