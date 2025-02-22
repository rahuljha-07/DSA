#include <vector>
#include <iostream>
using namespace std;

// same function works for both directed and undirected graph
void dfsUtil(int node, vector<vector<int>> &adj, vector<bool> &visited, vector<int> &dfs) {
    visited[node] = true;  // Mark the node as visited
    dfs.push_back(node);   // Add the node to the DFS traversal

    // Explore all neighbors
    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            dfsUtil(neighbor, adj, visited, dfs);
        }
    }
}

vector<int> dfsOfGraph(vector<vector<int>> &adj) {
    int V = adj.size();  // Number of vertices
    vector<int> dfs;     // To store DFS traversal
    vector<bool> visited(V, false);  // To track visited nodes

    // Start DFS from node 0 (assuming graph is connected)
    dfsUtil(0, adj, visited, dfs);

    return dfs;
}

int main() {
    // Example for Undirected Graph
    vector<vector<int>> undirectedAdj = {
        {1, 2},    // Neighbors of node 0
        {0, 3},    // Neighbors of node 1
        {0, 4},    // Neighbors of node 2
        {1, 5},    // Neighbors of node 3
        {2, 5},    // Neighbors of node 4
        {3, 4}     // Neighbors of node 5
    };

    vector<int> dfsUndirected = dfsOfGraph(undirectedAdj);
    cout << "DFS for Undirected Graph: ";
    for (int node : dfsUndirected) cout << node << " ";
    cout << endl;

    // Example for Directed Graph
    vector<vector<int>> directedAdj = {
        {1, 2},    // Node 0 points to 1, 2
        {3},       // Node 1 points to 3
        {4},       // Node 2 points to 4
        {5},       // Node 3 points to 5
        {},        // Node 4 points to no one
        {}         // Node 5 points to no one
    };

    vector<int> dfsDirected = dfsOfGraph(directedAdj);
    cout << "DFS for Directed Graph: ";
    for (int node : dfsDirected) cout << node << " ";
    cout << endl;

    return 0;
}
