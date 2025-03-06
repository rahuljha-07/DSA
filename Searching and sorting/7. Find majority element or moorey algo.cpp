#include <vector>

int majorityElement(vector<int>& arr) {
    // Variable to count occurrences and hold the candidate for majority element
    int count = 0;           // Counter for occurrences
    int candidate = 0;       // Potential majority element

    // Edge case: if the array contains only one element
    if (arr.size() == 1) return arr[0];

    // First pass: Find the candidate for majority element
    for (int i = 0; i < arr.size(); i++) {
        // If count is zero, select the current element as the candidate
        if (count == 0) {
            candidate = arr[i];
        }

        // Increment or decrement the count based on the candidate
        if (candidate == arr[i]) {
            count += 1; // Increase count if the current element is the candidate
        } else {
            count -= 1; // Decrease count if the current element is not the candidate
        }
    }

    // Second pass: Verify if the candidate is indeed the majority element
    count = 0; // Reset count to check the actual occurrences of the candidate
    for (int i = 0; i < arr.size(); i++) {
        if (candidate == arr[i]) {
            count++; // Count the occurrences of the candidate
        }
    }

    // Check if the count of the candidate is greater than n/2
    return (count > arr.size() / 2) ? candidate : -1; // Return candidate if it is the majority, else -1
}
