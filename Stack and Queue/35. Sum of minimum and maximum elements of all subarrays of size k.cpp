#include <iostream>
#include <vector>
#include <deque>

using namespace std;

// Function to calculate the sum of minimum and maximum elements of all subarrays of size k
long long sumOfMinAndMax(vector<int>& arr, int k) {
    int n = arr.size();
    if (n < k || k <= 0) return 0; // Return 0 if k is greater than n or non-positive

    deque<int> maxDeque; // Deque to store indices of maximum elements
    deque<int> minDeque; // Deque to store indices of minimum elements
    long long sum = 0; // Variable to store the total sum

    int i = 0, j = 0; // Initialize two pointers

    while (j < n) {
        // For max deque
        while (!maxDeque.empty() && maxDeque.back() < arr[j]) {
            maxDeque.pop_back(); // Remove smaller elements from the back
        }
        maxDeque.push_back(arr[j]); // Add current element

        // For min deque
        while (!minDeque.empty() && minDeque.back() > arr[j]) {
            minDeque.pop_back(); // Remove larger elements from the back
        }
        minDeque.push_back(arr[j]); // Add current element

        // If we have processed at least k elements
        if (j - i + 1 == k) {
            // The front of the maxDeque is the maximum for the current window
            // The front of the minDeque is the minimum for the current window
            sum += maxDeque.front() + minDeque.front(); // Add to sum

            // Move the window forward: remove the element going out of the window
            if (maxDeque.front() == arr[i]) {
                maxDeque.pop_front(); // Remove from max deque
            }
            if (minDeque.front() == arr[i]) {
                minDeque.pop_front(); // Remove from min deque
            }

            i++; // Move the start of the window
        }
        j++; // Move the end of the window
    }

    return sum; // Return the total sum
}

int main() {
    vector<int> arr = {1, 3, -1, -3, 5, 3, 6, 7}; // Example array
    int k = 3; // Size of the subarray
    long long result = sumOfMinAndMax(arr, k); // Call the function
    cout << "Sum of min and max of all subarrays of size " << k << ": " << result << endl; // Output the result
    return 0;
}
