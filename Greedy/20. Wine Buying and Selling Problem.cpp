#include <iostream>
#include <vector>
#include <cmath> // For abs function
using namespace std;

// Function to calculate the minimum cost of wine buying and selling
int wineSelling(vector<int>& arr, int n) {
    int buyer = 0, seller = 0; // Buyer and seller pointers
    int cost = 0; // Total cost

    // Iterate until all buying and selling are complete
    while (buyer < n && seller < n) {
        // Move buyer pointer to the next positive element (buyer)
        while (buyer < n && arr[buyer] <= 0) buyer++;

        // Move seller pointer to the next negative element (seller)
        while (seller < n && arr[seller] >= 0) seller++;

        // Break if no buyers or sellers are left
        if (buyer == n || seller == n) break;

        // Calculate the transaction
        int transaction = min(arr[buyer], -arr[seller]); // Max wine that can be transferred
        cost += abs(buyer - seller) * transaction;      // Add cost based on distance
        arr[buyer] -= transaction;                      // Reduce the buyer's demand
        arr[seller] += transaction;                     // Reduce the seller's supply
    }

    return cost; // Return the total cost
}

// Driver code
int main() {
    int n;
    cout << "Enter the number of houses: ";
    cin >> n;

    vector<int> arr(n);
    cout << "Enter the wine demands/supplies (positive for buying, negative for selling):\n";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Calculate and display the minimum cost
    cout << "Minimum cost of wine transactions: " << wineSelling(arr, n) << endl;

    return 0;
}
