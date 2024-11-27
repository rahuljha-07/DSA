//Kruskal's algorithm for MST
#include <bits/stdc++.h>
using namespace std;

// Structure to represent an edge in the graph
struct Edge {
    int u;      // Start node
    int v;      // End node
    int weight; // Weight of the edge (pipe diameter or digging cost)
};

// Comparator to sort edges by weight (ascending order)
bool compare(Edge a, Edge b) {
    return a.weight < b.weight;
}

// Disjoint Set Union (DSU) or Union-Find functions for Kruskal's Algorithm
class DSU {
    vector<int> parent, rank;

public:
    DSU(int n) {
        parent.resize(n + 1);
        rank.resize(n + 1, 0);
        for (int i = 0; i <= n; i++) {
            parent[i] = i; // Each node is its own parent initially
        }
    }

    int find(int x) {
        if (x != parent[x]) {
            parent[x] = find(parent[x]); // Path compression
        }
        return parent[x];
    }

    void unite(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
};

// Function to find the MST with wells and pipes
void waterConnectionProblem(int n, int p, vector<int>& a, vector<int>& b, vector<int>& d, vector<int>& wellCost) {
    vector<Edge> edges; // List of all edges

    // Add the pipes as edges
    for (int i = 0; i < p; i++) {
        edges.push_back({a[i], b[i], d[i]});
    }

    // Add edges for wells (connect all nodes to node 0)
    for (int i = 1; i <= n; i++) {
        edges.push_back({0, i, wellCost[i - 1]});
    }

    // Sort edges by weight
    sort(edges.begin(), edges.end(), compare);

    // Initialize DSU for Kruskal's algorithm
    DSU dsu(n);

    int totalCost = 0;
    vector<Edge> mstEdges; // To store the edges of the MST

    // Process edges in ascending order of weight
    for (auto edge : edges) {
        int u = edge.u;
        int v = edge.v;
        int weight = edge.weight;

        // Check if adding this edge creates a cycle
        if (dsu.find(u) != dsu.find(v)) {
            dsu.unite(u, v); // Merge the sets
            totalCost += weight; // Add the edge weight to total cost
            mstEdges.push_back(edge); // Add the edge to MST
        }
    }

    // Print the result
    cout << "Total cost of water connections: " << totalCost << endl;
    cout << "MST edges (Tank, Tap, Diameter/Cost):" << endl;
    for (auto edge : mstEdges) {
        if (edge.u == 0) {
            cout << "Well dug at house " << edge.v << " with cost " << edge.weight << endl;
        } else {
            cout << edge.u << " " << edge.v << " " << edge.weight << endl;
        }
    }
}

// Main function
int main() {
    int n = 9; // Number of houses
    int p = 6; // Number of pipes
    vector<int> a = {7, 5, 4, 2, 9, 3};
    vector<int> b = {4, 9, 6, 8, 7, 1};
    vector<int> d = {98, 72, 10, 22, 17, 66};
    vector<int> wellCost = {5, 8, 12, 15, 10, 8, 6, 4, 7}; // Cost of digging wells at each house

    waterConnectionProblem(n, p, a, b, d, wellCost);

    return 0;
}
