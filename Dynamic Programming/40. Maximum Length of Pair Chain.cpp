#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Custom comparator to sort pairs based on the second element
bool comp(pair<int, int>& a, pair<int, int>& b) {
    return a.second < b.second;  // Sort by the second element (ascending order)
}

int maxChainLen(vector<pair<int, int>>& v, int n) {
    // Step 1: Sort the pairs by the second element
    sort(v.begin(), v.end(), comp);

    // Step 2: Initialize variables for tracking the longest chain
    int count = 1;  // The first pair is always part of the chain
    int lastEnd = v[0].second;  // The end of the first pair in the chain

    // Step 3: Greedily check each pair
    for (int i = 1; i < n; i++) {
        if (v[i].first > lastEnd) {  // If the current pair can follow the previous one
            count++;
            lastEnd = v[i].second;  // Update the end of the chain
        }
    }

    return count;
}

int main() {
    // Example input
    vector<pair<int, int>> pairs = {{1, 2}, {2, 3}, {3, 4}, {5, 6}, {4, 7}};
    int n = pairs.size();

    // Find the maximum chain length
    cout << "Maximum chain length: " << maxChainLen(pairs, n) << endl;  // Output: 4

    return 0;
}
