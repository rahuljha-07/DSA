#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

// Function to process queries on an array
void bishopandsoldier(int n, int q, vector<int>& a) {
    // Sort the array in ascending order
    sort(a.begin(), a.end());

    // Create a prefix sum array
    vector<long long> pre(n + 1); // Use long long to handle large sums
    pre[0] = 0; // Initialize the first element of prefix sum as 0

    // Calculate the prefix sums
    for (int i = 1; i <= n; i++) {
        pre[i] = pre[i - 1] + a[i - 1]; // Cumulative sum up to index i
    }

    // Process each query
    while (q--) {
        int x; // Query value
        cin >> x; // Input the value for the query

        // Find the index of the first element greater than x
        int idx = upper_bound(a.begin(), a.end(), x) - a.begin(); // upper_bound returns an iterator, convert to index

        // Output the index and the prefix sum at that index
        cout << idx << " " << pre[idx] << endl;
    }
}

int main() {
    int n; // Number of elements in the array
    cin >> n; // Input the size of the array
    vector<int> a(n); // Declare the array of size n

    // Input the elements of the array
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int q; // Number of queries
    cin >> q; // Input the number of queries

    // Call the function to process queries
    bishopandsoldier(n, q, a);

    return 0; // Exit the program
}
