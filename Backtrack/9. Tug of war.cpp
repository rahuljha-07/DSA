#include <iostream>
#include <vector>
#include <cmath>
#include <climits>
using namespace std;

// Global variables to store the best partition and minimum difference
int minDifference = INT_MAX;
vector<int> bestSet1, bestSet2;

// Recursive function to solve the Tug of War problem
void solve(vector<int>& arr, int index, vector<int>& set1, vector<int>& set2, int sumSet1, int sumSet2) {
    // Base case: If all elements are placed
    if (index == arr.size()) {
        if (abs((int)set1.size() - (int)set2.size()) > 1) return; // Ensure valid partition size

        int delta = abs(sumSet1 - sumSet2);
        if (delta < minDifference) {
            minDifference = delta;
            bestSet1 = set1;
            bestSet2 = set2;
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
    cout << "Best Partition:\nSet 1: ";
    for (int num : bestSet1) cout << num << " ";
    cout << "\nSet 2: ";
    for (int num : bestSet2) cout << num << " ";
    cout << "\nMinimum Difference: " << minDifference << endl;

    return 0;
}