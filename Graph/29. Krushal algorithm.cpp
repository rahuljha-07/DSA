#include <bits/stdc++.h>
using namespace std;

//AYUSHI CODE
#include <iostream>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

// Function to find the parent of a node using path compression
int findparent(int element, vector<int>& ds) {
    if (element == ds[element]) 
        return element;
    return ds[element] = findparent(ds[element], ds);
}

// Function to execute Kruskal's Algorithm and return the total weight of the MST
int kruskal_mst(int V, const vector<vector<vector<int>>>& adj) {

    vector<int> ds(V); // Disjoint set for union-find
    vector<int> rank(V, 1); // Rank array for union by rank

    // Initialize each vertex as its own parent
    for (int i = 0; i < V; i++) ds[i] = i;

    // Priority queue to store edges in the form {weight, {u, v}}
    priority_queue<pair<int, pair<int, int>>, 
                   vector<pair<int, pair<int, int>>>, 
                   greater<pair<int, pair<int, int>>>> pq;

    // Input graph edges from the adjacency list into the priority queue
    for (int u = 0; u < V; u++) {
        for (const vector<int>& edge : adj[u]) {
            int v = edge[0]; // Destination vertex
            int weight = edge[1]; // Edge weight
            pq.push({weight, {u, v}});
        }
    }

    int count = 0; // Count of edges in the MST
    int sum = 0; // Sum of weights of edges in the MST

    // While MST does not contain V-1 edges
    while (count < V - 1 && !pq.empty()) {
        int dist = pq.top().first; // Weight of the edge
        int u = pq.top().second.first; // Source vertex of the edge
        int v = pq.top().second.second; // Destination vertex of the edge
        pq.pop();

        int p1 = findparent(u, ds); // Find the parent of u
        int p2 = findparent(v, ds); // Find the parent of v

        // If u and v belong to different sets, add the edge to MST
        if (p1 != p2) {// parents are different, so they are not in the same set i.e no cycle
            // Union by rank
            if (rank[p1] < rank[p2]) {
                ds[p1] = p2; // Make p2 the parent of p1
            } else if (rank[p2] < rank[p1]) {
                ds[p2] = p1; // Make p1 the parent of p2
            } else {
                ds[p1] = p2; // Make p2 the parent of p1
                rank[p2]++; // Increase rank of p2 as both were same rank
            }

            sum += dist; // Add edge weight to the total sum
            count++; // Increase the edge count for MST

            // Output the edge added to the MST
            cout << "Edge included in MST: " << u << " -> " << v 
                 << " with weight " << dist << endl;
        }
    }

    return sum; // Return the total weight of the MST
}

// Main function to drive the program
int main() {
    int V, E; // Number of vertices and edges

    cout << "Enter the number of vertices: ";
    cin >> V;

    cout << "Enter the number of edges: ";
    cin >> E;

    // Adjacency list to store the graph
    vector<vector<vector<int>>> adj(V);

    cout << "Enter edges in the format (u v weight): " << endl;
    for (int i = 0; i < E; i++) {
        int u, v, weight;
        cin >> u >> v >> weight;
        adj[u].push_back({v, weight});
        adj[v].push_back({u, weight}); // For undirected graph
    }

    // Execute Kruskal's Algorithm and get the MST weight
    int mstWeight = kruskal_mst(V, adj);

    // Output the total weight of the MST
    cout << "Total weight of the Minimum Spanning Tree: " << mstWeight << endl;

    return 0;
}








//same code from striver


class DisjointSet {
    vector<int> rank, parent, size;
public:
    DisjointSet(int n) {
        rank.resize(n + 1, 0);
        parent.resize(n + 1);
        size.resize(n + 1);
        for (int i = 0; i <= n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    int findUPar(int node) {
        if (node == parent[node])
            return node;
        return parent[node] = findUPar(parent[node]);
    }

    void unionByRank(int u, int v) {
        int ulp_u = findUPar(u);
        int ulp_v = findUPar(v);
        if (ulp_u == ulp_v) return;
        if (rank[ulp_u] < rank[ulp_v]) {
            parent[ulp_u] = ulp_v;
        }
        else if (rank[ulp_v] < rank[ulp_u]) {
            parent[ulp_v] = ulp_u;
        }
        else {
            parent[ulp_v] = ulp_u;
            rank[ulp_u]++;
        }
    }

    void unionBySize(int u, int v) {
        int ulp_u = findUPar(u);
        int ulp_v = findUPar(v);
        if (ulp_u == ulp_v) return;
        if (size[ulp_u] < size[ulp_v]) {
            parent[ulp_u] = ulp_v;
            size[ulp_v] += size[ulp_u];
        }
        else {
            parent[ulp_v] = ulp_u;
            size[ulp_u] += size[ulp_v];
        }
    }
};
class Solution
{
public:
    //Function to find sum of weights of edges of the Minimum Spanning Tree.
    int spanningTree(int V, vector<vector<int>> adj[])
    {
        // 1 - 2 wt = 5
        /// 1 - > (2, 5)
        // 2 -> (1, 5)

        // 5, 1, 2
        // 5, 2, 1
        vector<pair<int, pair<int, int>>> edges;
        for (int i = 0; i < V; i++) {
            for (auto it : adj[i]) {
                int adjNode = it[0];
                int wt = it[1];
                int node = i;

                edges.push_back({wt, {node, adjNode}});
            }
        }
        DisjointSet ds(V);
        sort(edges.begin(), edges.end());
        int mstWt = 0;
        for (auto it : edges) {
            int wt = it.first;
            int u = it.second.first;
            int v = it.second.second;

            if (ds.findUPar(u) != ds.findUPar(v)) {
                mstWt += wt;
                ds.unionBySize(u, v);
            }
        }

        return mstWt;
    }
};

int main() {

    int V = 5;
    vector<vector<int>> edges = {{0, 1, 2}, {0, 2, 1}, {1, 2, 1}, {2, 3, 2}, {3, 4, 1}, {4, 2, 2}};
    vector<vector<int>> adj[V];
    for (auto it : edges) {
        vector<int> tmp(2);
        tmp[0] = it[1];
        tmp[1] = it[2];
        adj[it[0]].push_back(tmp);

        tmp[0] = it[0];
        tmp[1] = it[2];
        adj[it[1]].push_back(tmp);
    }

    Solution obj;
    int mstWt = obj.spanningTree(V, adj);
    cout << "The sum of all the edge weights: " << mstWt << endl;
    return 0;
}