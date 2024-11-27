#include <bits/stdc++.h>
using namespace std;

int minimumPlatforms(int arr[], int dep[], int n) {
    // Step 1: Sort arrival and departure arrays
    sort(arr, arr + n);
    sort(dep, dep + n);

    // Step 2: Initialize variables
    int platforms_needed = 1; // Minimum 1 platform for the first train
    int result = 1;           // To store the final result
    int i = 1, j = 0;         // Pointers for arrival and departure

    // Step 3: Traverse arrival and departure arrays
    while (i < n && j < n) {
        // If next train arrives before the current one departs
        if (arr[i] <= dep[j]) {
            platforms_needed++; // Increase platform count
            i++;
        } else {
            // Train departs, reduce platform count
            platforms_needed--;
            j++;
        }

        // Update the result with the maximum platforms needed so far
        result = max(result, platforms_needed);
    }

    return result; // Return the minimum number of platforms required
}

// Main function
int main() {
    // Example 1
    int arr1[] = {900, 940, 950, 1100, 1500, 1800};
    int dep1[] = {910, 1200, 1120, 1130, 1900, 2000};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    cout << "Minimum Platforms Required: " << minimumPlatforms(arr1, dep1, n1) << endl;

    // Example 2
    int arr2[] = {900, 1235, 1100};
    int dep2[] = {1000, 1240, 1200};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    cout << "Minimum Platforms Required: " << minimumPlatforms(arr2, dep2, n2) << endl;

    // Example 3
    int arr3[] = {1000, 935, 1100};
    int dep3[] = {1200, 1240, 1130};
    int n3 = sizeof(arr3) / sizeof(arr3[0]);
    cout << "Minimum Platforms Required: " << minimumPlatforms(arr3, dep3, n3) << endl;

    return 0;
}

/*
Explanation:
Input Sorting:

The arr[] and dep[] arrays are sorted independently.
Sorting ensures that we can process events (arrival/departure) in chronological order.
Two-Pointer Approach:

i: Pointer for the next arrival in the arr[] array.
j: Pointer for the next departure in the dep[] array.
Logic:

If a train arrives (arr[i] <= dep[j]), increase the count of platforms needed.
If a train departs (arr[i] > dep[j]), reduce the count of platforms needed.
Update the maximum platforms required (result) at every step.
Edge Cases:

When two trains have the same arrival or departure times, the algorithm handles them correctly because both arrays are sorted.
Example Walkthrough (Example 1):
Input:
plaintext
Copy code
arr[] = {900, 940, 950, 1100, 1500, 1800}
dep[] = {910, 1200, 1120, 1130, 1900, 2000}
Sorted:
plaintext
Copy code
arr[] = {900, 940, 950, 1100, 1500, 1800}
dep[] = {910, 1120, 1130, 1200, 1900, 2000}
Execution:
i=1, j=0, platforms_needed=1
Train 2 arrives at 940. arr[i] <= dep[j] → platforms_needed = 2.
i=2, j=0, platforms_needed=2
Train 3 arrives at 950. arr[i] <= dep[j] → platforms_needed = 3.
i=3, j=0, platforms_needed=3
Train 1 departs at 910. arr[i] > dep[j] → platforms_needed = 2.
Continue processing...
Final result: 3.
Output:
plaintext
Copy code
Minimum Platforms Required: 3
*/