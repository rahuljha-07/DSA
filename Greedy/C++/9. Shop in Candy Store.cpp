#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Function to calculate the minimum and maximum cost
pair<int, int> candyStore(vector<int>& candies, int n, int k) {
    // Sort the candies prices in ascending order
    sort(candies.begin(), candies.end());

    // Calculate minimum cost
    int minCost = 0;
    int left = 0; // Pointer to buy candies from the start
    int right = n - 1; // Pointer to get candies for free from the end

    while (left <= right) {
        minCost += candies[left]; // Buy candy from the start
        left++; // Move to the next candy to buy
        right -= k; // Take k candies for free
    }

    // Calculate maximum cost
    int maxCost = 0;
    left = 0; // Pointer to get candies for free from the start
    right = n - 1; // Pointer to buy candies from the end

    while (left <= right) {
        maxCost += candies[right]; // Buy candy from the end
        right--; // Move to the next candy to buy
        left += k; // Take k candies for free
    }

    return {minCost, maxCost};
}

int main() {
    int n = 4; // Number of candies
    int k = 2; // Free candies per candy purchased
    vector<int> candies = {3, 2, 1, 4}; // Prices of candies

    // Calculate minimum and maximum cost
    pair<int, int> result = candyStore(candies, n, k);

    // Print the results
    cout << "Minimum cost: " << result.first << endl;
    cout << "Maximum cost: " << result.second << endl;

    return 0;
}
