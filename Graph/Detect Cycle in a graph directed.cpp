
#include <vector>
using namespace std;
// DFS

// Utility function to perform DFS and detect cycle
bool dfsUtil(int node, vector<vector<int>> &adj, vector<bool> &visited, vector<bool> &order) {
    visited[node] = true;  // Mark the node as visited
    order[node] = true;    // Add the node to the current recursion stack

    // Explore all neighbors
    for (int neighbor : adj[node]) {
        // If the neighbor is not visited, perform DFS on it
        if (!visited[neighbor]) {
            if (dfsUtil(neighbor, adj, visited, order)) {
                return true;  // Cycle detected
            }
        }
        // If the neighbor is already in the recursion stack, a cycle exists
        else if (order[neighbor]) {
            return true;  // Cycle detected
        }
    }

    // Remove the node from the recursion stack
    order[node] = false;
    return false;  // No cycle detected from this node
}

// Function to detect a cycle in a directed graph
bool isCyclic(vector<vector<int>> &adj) {
    int V = adj.size();  // Number of vertices
    vector<bool> visited(V, false);  // To track visited nodes
    vector<bool> order(V, false);    // To track nodes in the current recursion stack

    // Check for cycles in all components of the graph
    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            if (dfsUtil(i, adj, visited, order)) {
                return true;  // Cycle detected
            }
        }
    }

    return false;  // No cycle detected
}


// BFS

#include <vector>
#include <iostream>
#include <queue>
using namespace std;

// Function to perform topological sort using BFS and detect a cycle
bool hasCycleWithBFS(vector<vector<int>> &adj) {
    int V = adj.size();         // Number of vertices
    vector<int> indegree(V, 0); // To store in-degrees of all nodes

    // Calculate in-degrees of all nodes
    for (int i = 0; i < V; i++) {
        for (int neighbor : adj[i]) {
            indegree[neighbor]++;
        }
    }

    // Queue for nodes with in-degree 0
    queue<int> q;
    for (int i = 0; i < V; i++) {
        if (indegree[i] == 0) {
            q.push(i);
        }
    }

    vector<int> topoOrder; // To store the topological order
    int count = 0;         // Count of processed nodes

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        topoOrder.push_back(node); // Add the node to topological order
        count++;

        // Decrease the in-degree of neighbors
        for (int neighbor : adj[node]) {
            indegree[neighbor]--;
            if (indegree[neighbor] == 0) {
                q.push(neighbor); // Add neighbors with in-degree 0 to the queue
            }
        }
    }

    // If the count of processed nodes is less than the number of vertices, there is a cycle
    if (count != V) {
        return true; // Cycle detected
    }

    // Print the topological order if no cycle
    cout << "Topological Order: ";
    for (int node : topoOrder) {
        cout << node << " ";
    }
    cout << endl;

    return false; // No cycle detected
}

int main() {
    // Example directed graph with a cycle
    vector<vector<int>> directedAdj = {
        {1, 2},    // Node 0 points to 1, 2
        {3},       // Node 1 points to 3
        {3, 4},    // Node 2 points to 3, 4
        {},        // Node 3 points to no one
        {5},       // Node 4 points to 5
        {2}        // Node 5 points to 2 (Cycle)
    };

    if (hasCycleWithBFS(directedAdj)) {
        cout << "The graph contains a cycle." << endl;
    } else {
        cout << "The graph does not contain a cycle." << endl;
    }

    return 0;
}
