#include <vector>
#include <algorithm>
using namespace std;

int minSwaps(vector<int>& nums) {
    int n = nums.size(); // Step 1: Get the size of the input array
    vector<pair<int, int>> v(n); // Step 2: Create a vector of pairs to store numbers and their original indices
    
    // Step 3: Fill the vector with pairs of (element value, original index)
    for (int i = 0; i < n; i++) 
        v[i] = {nums[i], i};

    // Step 4: Sort the vector based on the first element of the pairs (the original numbers)
    sort(v.begin(), v.end());

    int c = 0; // Step 5: Initialize a counter for swaps

    // Step 6: Iterate through the sorted array to find misplaced elements
    for (int i = 0; i < n;) {
        // If the current element is in its correct position
        if (v[i].second == i) {
            i++; // Move to the next element
        } else {
            // If the current element is not in the correct position, perform a swap
            c++; // Increment the swap counter
            swap(v[i], v[v[i].second]); // Swap the current element with the element at its original index
            // Note: Do not increment i here to check the new element at the current position
        }
    }

    // Step 7: Return the total number of swaps required
    return c;
}
