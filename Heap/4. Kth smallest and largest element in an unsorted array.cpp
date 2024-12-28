#include <iostream>
#include <vector>
#include <queue>
using namespace std;

pair<int, int> findKthSmallestAndLargest(vector<int>& nums, int k) {
    // Min-heap to store the k largest elements (for the k-th largest element)
    priority_queue<int, vector<int>, greater<int>> minHeap;

    // Max-heap to store the k smallest elements (for the k-th smallest element)
    priority_queue<int> maxHeap;

    int counter = 0;  // Counter to track the number of elements added to the heaps

    // Iterate through all elements in the array
    for (int num : nums) {
        // For k-th largest: Maintain a min-heap of size k
        minHeap.push(num);
        // For k-th smallest: Maintain a max-heap of size k
        maxHeap.push(num);

        counter++;  // Increment counter after adding an element
        if (counter > k) {
            minHeap.pop();  // Remove the smallest element if heap size exceeds k
        }

        
        if (counter > k) {
            maxHeap.pop();  // Remove the largest element if heap size exceeds k
        }
    }

    // The root of the min-heap now contains the k-th largest element
    // The root of the max-heap now contains the k-th smallest element
    return {maxHeap.top(), minHeap.top()};
}

int main() {
    vector<int> arr = {3, 2, 1, 5, 6, 4};
    int k = 2;
    
    pair<int, int> result = findKthSmallestAndLargest(arr, k);
    
    cout << "The " << k << "th smallest element is: " << result.first << endl;
    cout << "The " << k << "th largest element is: " << result.second << endl;

    return 0;
}
