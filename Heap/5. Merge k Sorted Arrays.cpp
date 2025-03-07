#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<int> mergeKArrays(vector<vector<int>>& arr, int k) { //with tuple
    // Define a type to store: (value, row index, column index)
    typedef tuple<int, int, int> triplet;
    
    // Vector to store the result
    vector<int> ans;

    // Min-heap priority_queue (smallest element on top)
    // We use tuple comparison: the first element in the tuple (value) determines the order
    priority_queue<triplet, vector<triplet>, greater<triplet>> q;

    // Step 1: Push the first element of each array into the priority queue
    for (int i = 0; i < k; i++) {
        // Push (value, row index, column index) into the heap
        q.push({arr[i][0], i, 0});
    }

    // Step 2: Process the priority queue
    while (!q.empty()) {
        // Get the smallest element from the heap (which will be the top of the heap)
        triplet temp = q.top();
        q.pop();

        // Add the smallest element to the result vector
        ans.push_back(get<0>(temp));  // Get the value from the tuple

        // Extract the row index and column index from the tuple
        int row = get<1>(temp);  // Row index (which array the element came from)
        int col = get<2>(temp);  // Column index (position in the array)

        // Step 3: If there are more elements in the current array, push the next element to the heap
        col++;  // Move to the next element in the array

        // If the index is within the bounds of the array, push the next element into the heap
        if (col < arr[row].size()) {
            q.push({arr[row][col], row, col});
        }
    }

    // Step 4: Return the merged sorted array
    return ans;
}


vector<int> mergeKArrays(vector<vector<int>>& arr, int k) { //with pair
    // The priority_queue stores a tuple of (value, {array index, index within that array})
    typedef pair<int, pair<int, int>> p;

    // This will store the final merged array
    vector<int> ans;

    // Min-heap priority_queue
    // The 'greater<p>' ensures that the smallest element is always at the top of the heap
    priority_queue<p, vector<p>, greater<p>> q;

    // Step 1: Push the first element of each array into the priority queue
    for (int i = 0; i < k; i++) {
        // Push the first element of each array, along with its array index and element index
        q.push({arr[i][0], {i, 0}});
    }

    // Step 2: Process the priority queue
    while (!q.empty()) {
        // Get the smallest element from the heap (which will be the top of the heap)
        p temp = q.top();
        q.pop();

        // Add the smallest element to the result vector
        ans.push_back(temp.first);

        // Extract array index and element index from the pair
        int row = temp.second.first;  // The index of the array
        int col = temp.second.second;  // The index of the element in the array

        // Step 3: If there are more elements in the current array, push the next element to the heap
        col++;  // Move to the next element in the array

        // If the index is within the array bounds, push the next element into the priority queue
        if (col < arr[row].size()) {
            q.push({arr[row][col], {row, col}});
        }
    }

    // Step 4: Return the merged sorted array
    return ans;
}
int main() {
    vector<vector<int>> arrays = {
        {1, 4, 7},
        {2, 5, 8},
        {3, 6, 9}
    };

    // Merging the k sorted arrays
    vector<int> result = mergeKArrays(arrays, arrays.size());

    // Output the merged result
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
