#include <iostream>
#include <vector>
#include <cmath>
#include <climits>
using namespace std;

// Global variables to store the minimum difference and the answer
int minDifference = INT_MAX;
string bestPartition = "";

// Recursive function to solve the Tug of War problem
void solve(vector<int>& arr, int index, vector<int>& set1, vector<int>& set2, int sumSet1, int sumSet2) {
    // Base case: when all elements have been considered
    if (index == arr.size()) {
        int delta = abs(sumSet1 - sumSet2); // Calculate the difference between the sums
        // Update the best solution if a smaller difference is found
        if (delta < minDifference) {
            minDifference = delta;
            bestPartition = "{Set1: ";
            for (int num : set1) bestPartition += to_string(num) + " ";
            bestPartition += "} {Set2: ";
            for (int num : set2) bestPartition += to_string(num) + " ";
            bestPartition += "}";
        }
        return;
    }

    // Include the current element in set1 if its size is within the limit
    if (set1.size() < (arr.size() + 1) / 2) {
        set1.push_back(arr[index]);
        solve(arr, index + 1, set1, set2, sumSet1 + arr[index], sumSet2);
        set1.pop_back(); // Backtrack
    }

    // Include the current element in set2 if its size is within the limit
    if (set2.size() < (arr.size() + 1) / 2) {
        set2.push_back(arr[index]);
        solve(arr, index + 1, set1, set2, sumSet1, sumSet2 + arr[index]);
        set2.pop_back(); // Backtrack
    }
}

int main() {
    // Input array
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7, 8};
    
    // Vectors to store the two sets
    vector<int> set1, set2;
    
    // Solve the problem starting with index 0 and empty sets
    solve(arr, 0, set1, set2, 0, 0);

    // Print the best partition and the minimum difference
    cout << "Best Partition: " << bestPartition << endl;
    cout << "Minimum Difference: " << minDifference << endl;

    return 0;
}
