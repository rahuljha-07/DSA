#include <vector>
#include <iostream>
#include <stack>
using namespace std;

// Helper function to perform DFS and store nodes in topological order
void topoSortUtil(int node, vector<vector<int>> &adj, vector<bool> &visited, stack<int> &topoStack) {
    visited[node] = true;  // Mark the node as visited

    // Explore all neighbors
    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            topoSortUtil(neighbor, adj, visited, topoStack);
        }
    }

    // Push the node into the stack after exploring all its neighbors
    topoStack.push(node);
}

vector<int> topologicalSort(vector<vector<int>> &adj) {
    int V = adj.size();  // Number of vertices
    vector<bool> visited(V, false);  // To track visited nodes
    stack<int> topoStack;  // Stack to store topological order

    // Perform DFS for all unvisited nodes
    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            topoSortUtil(i, adj, visited, topoStack);
        }
    }

    // Extract nodes from the stack to get the topological order
    vector<int> topoOrder;
    while (!topoStack.empty()) {
        topoOrder.push_back(topoStack.top());
        topoStack.pop();
    }

    return topoOrder;
}

int main() {
    // Example for Directed Acyclic Graph (DAG)
    vector<vector<int>> directedAdj = {
        {1, 2},    // Node 0 points to 1, 2
        {3},       // Node 1 points to 3
        {3, 4},    // Node 2 points to 3, 4
        {},        // Node 3 points to no one
        {5},       // Node 4 points to 5
        {}         // Node 5 points to no one
    };

    vector<int> topoOrder = topologicalSort(directedAdj);
    cout << "Topological Sort for Directed Graph: ";
    for (int node : topoOrder) cout << node << " ";
    cout << endl;

    return 0;
}
