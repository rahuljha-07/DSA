#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// Function to find the k-th largest sum of a contiguous subarray
int kthLargestSum(const vector<int>& arr, int k) {
    int n = arr.size();
    
    // Max-heap to store subarray sums
    priority_queue<int> maxHeap;
    
    // Traverse all subarrays and calculate their sums
    for (int i = 0; i < n; ++i) {
        int sum = 0;
        for (int j = i; j < n; ++j) {
            sum += arr[j];  // Calculate sum of subarray arr[i...j]
            
            // Push the sum into the max-heap
            maxHeap.push(sum);
            
            // If the size of the heap exceeds k, remove the top (largest element)
            if (maxHeap.size() > k) {
                maxHeap.pop();
            }
        }
    }
    
    // The top of the max-heap is the k-th largest sum
    return maxHeap.top();
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};  // Example input array
    int k = 3;  // We want to find the 3rd largest sum
    
    cout << "The " << k << "-th largest sum is: " << kthLargestSum(arr, k) << endl;

    return 0;
}
