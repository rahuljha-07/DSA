#include <bits/stdc++.h>
using namespace std;

// Helper function for backtracking
bool helper(int startIndex, int arr[], bool visited[], int k, int currentSum, int targetSum, int n) {
    // If only one subset is left, the rest of the elements will automatically form a valid subset
    if (k == 1) 
        return true;

    // If the current subset's sum reaches the target, move to the next subset
    if (currentSum == targetSum) {
        return helper(0, arr, visited, k - 1, 0, targetSum, n);
    }

    // Explore all elements in the array
    for (int i = startIndex; i < n; i++) {
        // If the current element is not visited and can be added to the current subset
        if (!visited[i]) {
            visited[i] = true; // Choose the current element

            // Recur for the next element
            if (helper(i + 1, arr, visited, k, currentSum + arr[i], targetSum, n)) {
                return true;
            }

            visited[i] = false; // Backtrack
        }
    }

    return false;
}

// Main function to check if partitioning is possible
bool isKPartitionPossible(int arr[], int n, int k) {
    int sum = accumulate(arr, arr + n, 0); // Calculate the sum of the array

    // If total sum is not divisible by k, partitioning is not possible
    if (k == 0 || sum % k != 0) 
        return false;

    int targetSum = sum / k; // Each subset must sum to this value
    bool visited[n] = {false}; // Array to track visited elements

    // Start backtracking
    return helper(0, arr, visited, k, 0, targetSum, n);
}

int main() {
    int arr[] = {2, 1, 4, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    int k = 3;

    if (isKPartitionPossible(arr, n, k)) {
        cout << "1 (Partitioning is possible)" << endl;
    } else {
        cout << "0 (Partitioning is not possible)" << endl;
    }

    return 0;
}