int minSubarraySum(vector<int>& arr) {
    int mini = INT_MAX; // Initialize to the largest possible value
    int sum = 0;        // Tracks the current sum of the subarray

    for (int i = 0; i < arr.size(); i++) {
        sum += arr[i];            // Add the current element to the sum
        mini = min(mini, sum);    // Update the minimum sum encountered so far

        if (sum > 0) sum = 0;     // Reset the sum if it becomes positive
    }

    return mini; // Return the smallest sum found
}
