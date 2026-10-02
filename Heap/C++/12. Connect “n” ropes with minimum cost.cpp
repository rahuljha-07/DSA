#include <iostream>
#include <queue>
using namespace std;

// Function to calculate the minimum cost of combining the elements in the array
long long minCost(long long arr[], long long n) {
    // Create a min heap (priority queue) to store the elements in increasing order
    priority_queue<long long, vector<long long>, greater<long long>> minHeap;

    long long totalCost = 0;  // Variable to store the total cost

    // Push all elements of the array into the min heap
    for(long long i = 0; i < n; i++) {
        minHeap.push(arr[i]);
    }

    // While there is more than one element in the heap, we keep combining the smallest two
    while(minHeap.size() > 1) {
        // Extract the two smallest elements from the heap
        long long firstMin = minHeap.top();  // Get the smallest element
        minHeap.pop();  // Remove the smallest element

        long long secondMin = minHeap.top();  // Get the second smallest element
        minHeap.pop();  // Remove the second smallest element

        // Calculate the cost to combine these two elements and add it to the total cost
        long long cost = firstMin + secondMin;
        totalCost += cost;

        // Push the combined element back into the heap
        minHeap.push(cost);
    }

    // Return the total cost of combining the elements
    return totalCost;
}

int main() {
    // Example usage of the function
    long long arr[] = {4, 3, 2, 6};
    long long n = sizeof(arr) / sizeof(arr[0]);

    long long result = minCost(arr, n);
    cout << "The minimum cost to combine all elements is: " << result << endl;

    return 0;
}
