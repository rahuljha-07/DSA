#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

// Alias for priority queue elements: (value, (array index, element index))
typedef pair<int, pair<int, int>> p;

// Function to find the smallest range that includes at least one element from each list
pair<int, int> findSmallestRange(vector<vector<int>>& arr, int n, int k) {
    priority_queue<p, vector<p>, greater<p>> minHeap;
    pair<int, int> ans;
    int range = INT_MAX;
    int maxi = INT_MIN;

    // Step 1: Push the first element of each array into the heap
    for (int i = 0; i < k; i++) {
        minHeap.push({arr[i][0], {i, 0}});  // (value, (row, col))
        maxi = max(maxi, arr[i][0]);
    }

    // Step 2: Process the heap
    while (!minHeap.empty()) {
        p temp = minHeap.top();
        minHeap.pop();

        int mini = temp.first;   // Current min element in the heap
        int row = temp.second.first;
        int col = temp.second.second;

        // Update range if a smaller range is found
        if (maxi - mini < range) {
            range = maxi - mini;
            ans = {mini, maxi};
        }

        // Step 3: Get the next element in the same row
        col++;
        if (col < n) {
            minHeap.push({arr[row][col], {row, col}});
            maxi = max(maxi, arr[row][col]);
        } else {
            // If any row runs out of elements, stop the process
            break;
        }
    }

    return ans;  // Return the smallest range found
}

int main() {
    // Sample input: 3 sorted lists of size 5 each
    vector<vector<int>> arr = {
        {1, 3, 5, 7, 9},
        {0, 2, 4, 6, 8},
        {2, 3, 5, 7, 11}
    };

    int n = arr[0].size();  // Number of elements in each list
    int k = arr.size();     // Number of lists

    pair<int, int> result = findSmallestRange(arr, n, k);
    
    cout << "Smallest Range: " << result.first << " " << result.second << endl;

    return 0;
}
