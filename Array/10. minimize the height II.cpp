// Approach
// Sort the Array: Sorting helps to handle the smallest and largest elements systematically.
// Initial Difference: Calculate the initial difference between the tallest and shortest towers before any operations.
// Iterate and Adjust Heights: For each tower, calculate the new possible heights after either increasing or decreasing by K. Ensure that no height becomes negative.
// Minimize the Difference: While iterating, we compute the difference between the maximum and minimum tower heights after the operation and keep track of the minimum possible difference.
// ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

// Key Points:
// We have to add or subtract K from each element.
// After sorting, the minimum difference will depend on the difference between the largest and smallest possible heights after the operations.
// ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
int getMinDiff(vector<int>& arr, int k) {
    int n = arr.size();
    if (n == 1) return 0;  // If there's only one tower, difference is 0.
    
    // Sort the array to handle elements in order.
    sort(arr.begin(), arr.end());

    // Initialize the result as the difference between the max and min height in the sorted array.
    int result = arr[n - 1] - arr[0];

    // The smallest possible height and largest possible height after adjusting with k
    int smallest = arr[0] + k;
    int largest = arr[n - 1] - k;

    // Traverse through the array to explore the different possibilities
    for (int i = 0; i < n - 1; i++) {
        int minHeight = min(smallest, arr[i + 1] - k);
        int maxHeight = max(largest, arr[i] + k);
        
        // If the new height is negative, skip to avoid invalid cases
        if (minHeight < 0) continue;

        // Update the result with the minimum possible difference
        result = min(result, maxHeight - minHeight);
    }

    return result;
}