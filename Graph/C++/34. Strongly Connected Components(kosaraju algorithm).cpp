#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

// Function to perform DFS and fill the stack for topo sort
void topoSort(int node, vector<int> adj[], vector<bool> &visited, stack<int> &st) {
    visited[node] = true;
    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            topoSort(neighbor, adj, visited, st);
        }
    }
    st.push(node);
}

// Function to perform DFS and collect nodes of a strongly connected component
void dfs(int node, vector<int> transpose[], vector<bool> &visited, vector<int> &component) {
    visited[node] = true;
    component.push_back(node);
    for (int neighbor : transpose[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor, transpose, visited, component);
        }
    }
}

int kosaraju(int V, vector<int> adj[]) {
    // Step 1: Toposort
    stack<int> st;
    vector<bool> visited(V, false);

    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            topoSort(i, adj, visited, st);
        }
    }

    // Step 2: Reverse the graph
    vector<int> transpose[V];
    for (int i = 0; i < V; i++) {
        for (int neighbor : adj[i]) {
            transpose[neighbor].push_back(i);
        }
    }

    // Step 3: DFS on the reversed graph
    fill(visited.begin(), visited.end(), false);
    int sccCount = 0; // Count of strongly connected components

    while (!st.empty()) {
        int node = st.top();
        st.pop();
        if (!visited[node]) {
            vector<int> component; // To store the current SCC
            dfs(node, transpose, visited, component);

            // Print the current SCC
            cout << "Strongly Connected Component " << ++sccCount << ": ";
            for (int v : component) {
                cout << v << " ";
            }
            cout << endl;
        }
    }

    return sccCount; // Return the number of SCCs
}

int main() {
    int V = 5; // Number of vertices
    vector<int> adj[V];

    // Example graph
    adj[0].push_back(1);
    adj[1].push_back(2);
    adj[2].push_back(0);
    adj[1].push_back(3);
    adj[3].push_back(4);

    cout << "Number of Strongly Connected Components: " << kosaraju(V, adj) << endl;

    return 0;
}
