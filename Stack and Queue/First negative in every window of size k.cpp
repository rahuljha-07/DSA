#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// Function to find the first negative integer in every window of size k
vector<long long> printFirstNegativeInteger(long long int arr[], long long int n, long long int k) {
    vector<long long> ans; // Vector to store the results
    queue<long> q; // Queue to store negative integers in the current window
    long long i = 0, j = 0; // i: start index of the window, j: end index of the window

    // Loop until the end of the array is reached
    while (j < n) {
        // If the current element is negative, add it to the queue
        if (arr[j] < 0) { 
            q.push(arr[j]);
        }

        // If the size of the current window is less than k, just expand the window
        if (j - i + 1 < k) {
            j++;  
        } 
        // When the size of the window reaches k
        else if (j - i + 1 == k) {
            // If there are no negative integers in the queue
            if (q.empty()) { 
                ans.push_back(0); // Add 0 to the answer vector
            }
            // If there are negative integers in the queue
            else {
                ans.push_back(q.front()); // Add the first negative integer to the answer
                // If the element that is being removed from the window is the same as the front of the queue
                if (arr[i] == q.front()) {
                    q.pop(); // Remove it from the queue
                }
            }
            // Move the window forward
            i++; // Increment the start index
            j++; // Increment the end index
        }
    }
    return ans; // Return the vector containing the first negative integers for each window
}

// Example usage
int main() {
    long long arr[] = {12, -1, -7, 8, -15, 30, 16, 28}; // Sample array
    long long n = sizeof(arr) / sizeof(arr[0]); // Size of the array
    long long k = 3; // Size of the window
    vector<long long> result = printFirstNegativeInteger(arr, n, k); // Call the function

    // Print the result
    for (long long x : result) {
        cout << x << " "; // Output each first negative integer
    }
    cout << endl;

    return 0;
}
