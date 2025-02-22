#include <iostream>
#include <vector>
#include <queue>
#include <numeric> // for accumulate()
using namespace std;

// Perform DFS to find connected components
void dfs(int node, vector<int> adj[], vector<bool> &visited, int &size) {
    visited[node] = true;
    size++;
    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor, adj, visited, size);
        }
    }
}

int journeyToMoon(int n, vector<vector<int>> astronaut) {
    // Step 1: Build the adjacency list
    vector<int> adj[n];
    for (auto &pair : astronaut) {
        adj[pair[0]].push_back(pair[1]);
        adj[pair[1]].push_back(pair[0]);
    }

    // Step 2: Find connected components using DFS
    vector<bool> visited(n, false);
    vector<int> sizes; // Sizes of connected components

    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            int size = 0;
            dfs(i, adj, visited, size);
            sizes.push_back(size);
        }
    }

    // Step 3: Calculate total pairs
    long long totalPairs = (long long)n * (n - 1) / 2; //nC2 = n*(n-1) /2

    // Step 4: Subtract invalid pairs (within the same country)
    long long invalidPairs = 0;
    for (int size : sizes) {
        invalidPairs += (long long)size * (size - 1) / 2;
    }

    // Valid pairs are total pairs minus invalid pairs
    return totalPairs - invalidPairs;
}

// Main function for testing
int main() {
    // Sample Input 0
    int n = 5; // Number of astronauts
    vector<vector<int>> astronaut = {{0, 1}, {2, 3}, {0, 4}};

    cout << "Valid pairs: " << journeyToMoon(n, astronaut) << endl;

    // Sample Input 1
    n = 4;
    astronaut = {{0, 2}};
    cout << "Valid pairs: " << journeyToMoon(n, astronaut) << endl;

    return 0;
}
