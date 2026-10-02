#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

// Function to perform DFS and find bridges using Tarjan's Algorithm
void dfs(int u, int &timer, vector<int> &disc, vector<int> &low, vector<vector<int>> &g, 
         int parent, vector<pair<int, int>> &bridges) {
    
    disc[u] = low[u] = timer; // Initialize discovery and low values
    timer++; // Increment the timer for the next call

    // Explore all the adjacent vertices of u
    for (int v : g[u]) {
        if (v == parent) 
            continue; // Ignore the edge to the parent vertex

        if (disc[v] == -1) { // If v is not visited
            dfs(v, timer, disc, low, g, u, bridges); // Recur for the child vertex
            
            // After recursion, update the low-link value of u
            low[u] = min(low[u], low[v]);

            // Check if the edge u-v is a bridge
            if (low[v] > disc[u]) {
                bridges.push_back({u, v});
            }
        } 
        else {
            // If v is already visited and is not the parent, update low[u]
            low[u] = min(low[u], disc[v]);
        }
    }
}


int main() {
    int n, m;
    cin >> n >> m;                 // number of nodes and edges
    vector<vector<int>> g(n);

    // Read edges (0-indexed). If your input is 1-indexed, uncomment the --u; --v;
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        // --u; --v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    // Optional: keep traversal deterministic
    for (int i = 0; i < n; ++i) sort(g[i].begin(), g[i].end());

    vector<int> disc(n, -1), low(n, -1);
    vector<pair<int,int>> bridges;
    int timer = 0;

    // Handle disconnected graphs
    for (int i = 0; i < n; ++i) {
        if (disc[i] == -1) {
            dfs(i, timer, disc, low, g, -1, bridges);
        }
    }

    // Normalize each bridge to (min, max) and sort for stable output
    for (auto &e : bridges) {
        if (e.first > e.second) swap(e.first, e.second);
    }
    sort(bridges.begin(), bridges.end());

    // Output
    cout << bridges.size() << "\n";
    for (auto &e : bridges) {
        cout << e.first << " " << e.second << "\n";
    }
    return 0;
}


// Function to perform DFS and find articulation points using Tarjan's Algorithm
void dfs(int u, int &timer, vector<int> &disc, vector<int> &low, vector<vector<int>> &g, 
         int parent, vector<pair<int, int>> &bridges, set<int> &articulationPoints) {

    disc[u] = low[u] = timer; // Initialize discovery and low values
    timer++; // Increment the timer for the next call
    int children = 0; // Count of children in the DFS tree

    // Explore all the adjacent vertices of u
    for (int v : g[u]) {
        if (v == parent) 
            continue; // Ignore the edge to the parent vertex

        if (disc[v] == -1) { // If v is not visited
            dfs(v, timer, disc, low, g, u, bridges, articulationPoints); // Recur for the child vertex
            children++; // Increase child count for u

            // After recursion, update the low-link value of u
            low[u] = min(low[u], low[v]);

            // Check if the edge u-v is a bridge
            if (low[v] > disc[u]) {
                bridges.push_back({u, v});
            }

            // Check if u is an articulation point (excluding the root case separately)
            if (parent != -1 && low[v] >= disc[u]) {
                articulationPoints.insert(u);
            }
        } 
        else {
            // If v is already visited and is not the parent, update low[u]
            low[u] = min(low[u], disc[v]);
        }
    }

    // Special case for the root vertex
    if (parent == -1 && children > 1) {
        articulationPoints.insert(u);
    }
}

int main() {
    int n, m;
    cin >> n >> m;                 // number of nodes and edges
    vector<vector<int>> g(n);

    // Read edges (0-indexed). If your input is 1-indexed, uncomment the --u; --v;
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        // --u; --v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    // Optional: keep traversal deterministic
    for (int i = 0; i < n; ++i) sort(g[i].begin(), g[i].end());

    vector<int> disc(n, -1), low(n, -1);
    vector<pair<int,int>> bridges;
    set<int> articulationPoints;
    int timer = 0;

    // Handle disconnected graphs
    for (int i = 0; i < n; ++i) {
        if (disc[i] == -1) {
            dfs(i, timer, disc, low, g, -1, bridges, articulationPoints);
        }
    }

    // Normalize each bridge to (min, max) and sort for stable output
    for (auto &e : bridges) {
        if (e.first > e.second) swap(e.first, e.second);
    }
    sort(bridges.begin(), bridges.end());

    // Output bridges
    cout << bridges.size() << "\n";
    for (auto &e : bridges) {
        cout << e.first << " " << e.second << "\n";
    }

    // Output articulation points (already ordered by set)
    cout << articulationPoints.size() << "\n";
    for (int u : articulationPoints) {
        cout << u << "\n";
    }

    return 0;
}
