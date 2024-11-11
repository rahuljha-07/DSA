#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int findKthLargest(vector<int>& nums, int k) {
    // Min-heap to store the largest k elements
    priority_queue<int, vector<int>, greater<int>> minHeap;
    int counter = 0;  // Counter to track the number of elements added to the heap

    // Iterate through all elements in the array
    for (int num : nums) {
        minHeap.push(num);  // Add current number to the heap
        counter++;  // Increment counter after adding an element

        // Once we have more than k elements, remove the smallest element
        if (counter > k) {
            minHeap.pop();
        }
    }

    // The root of the heap now contains the k-th largest element
    return minHeap.top();
}

int main() {
    vector<int> arr = {3, 2, 1, 5, 6, 4};
    int k = 2;
    int kthLargest = findKthLargest(arr, k);

    cout << "The " << k << "th largest element is: " << kthLargest << endl;
    return 0;
}
