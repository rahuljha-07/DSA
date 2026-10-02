#include <iostream>
#include <vector>
#include <climits>
using namespace std;

void tspBacktrack(vector<vector<int>>& cost, vector<bool>& visited, int currCity, int n, int count, int currCost, int& minCost) {
    // Base case: If all cities are visited, return to the starting city
    if (count == n) {
        // Add the cost to return to the starting city (0)
        currCost += cost[currCity][0];
        minCost = min(minCost, currCost); // Update the minimum cost
        return;
    }

    // Explore all possible cities
    for (int nextCity = 0; nextCity < n; nextCity++) {
        if (!visited[nextCity] && cost[currCity][nextCity] > 0) { // Check if city is unvisited and valid
            // Mark the city as visited
            visited[nextCity] = true;

            // Recur with the next city
            tspBacktrack(cost, visited, nextCity, n, count + 1, currCost + cost[currCity][nextCity], minCost);

            // Backtrack: Mark the city as unvisited
            visited[nextCity] = false;
        }
    }
}

int travellingSalesman(vector<vector<int>>& cost) {
    int n = cost.size();
    vector<bool> visited(n, false); // To keep track of visited cities
    visited[0] = true; // Start from city 0

    int minCost = INT_MAX;
    tspBacktrack(cost, visited, 0, n, 1, 0, minCost); // Start from city 0 with 0 cost

    return minCost;
}

int main() {
    vector<vector<int>> cost = {
        {0, 10, 15, 20},
        {10, 0, 35, 25},
        {15, 35, 0, 30},
        {20, 25, 30, 0}
    };

    cout << "The minimum cost of the tour is: " << travellingSalesman(cost) << endl;
    return 0;
}
