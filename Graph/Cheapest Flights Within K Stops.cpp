#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int K) {
    // Step 1: Build the adjacency list
    vector<vector<pair<int, int>>> graph(n);
    for (auto& flight : flights) {
        int u = flight[0], v = flight[1], w = flight[2];
        graph[u].push_back({v, w}); // Use push_back to add edges
    }

    // Step 2: Min-heap priority queue (cost, node, remaining stops)
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> pq;
    pq.push({0, src, 0}); // Push initial state (cost, src, 0 stops)

    // Step 3: Distance array to track the minimum cost to reach a node
    vector<int> dist(n, INT_MAX);
    dist[src] = 0;

    // Step 4: Perform BFS with priority queue
    while (!pq.empty()) {
        auto [cost, node, stops] = pq.top();
        pq.pop();

        // If we reach the destination, return the cost
        if (node == dst) return cost;

        // If stops exceed K, continue to the next iteration
        if (stops > K) continue;

        // Explore neighbors
        for (auto& neighbor : graph[node]) {
            int nextNode = neighbor.first;
            int price = neighbor.second;

            // Only proceed if this path offers a cheaper cost
            if (cost + price < dist[nextNode]) {
                dist[nextNode] = cost + price;
                pq.push({cost + price, nextNode, stops + 1});
            }
        }
    }

    // If no route is found, return -1
    return -1;
}

int main() {
    int n = 4; // Number of cities
    vector<vector<int>> flights = {{0, 1, 100}, {1, 2, 100}, {2, 3, 100}, {0, 2, 500}};
    int src = 0, dst = 3, K = 1;

    cout << "Cheapest Price: " << findCheapestPrice(n, flights, src, dst, K) << endl;

    return 0;
}
