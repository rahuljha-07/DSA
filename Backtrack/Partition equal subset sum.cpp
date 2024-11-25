#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

// Helper function for the recursive top-down approach
bool subsetSumTopDownHelper(int arr[], int n, int sum, vector<vector<int>>& t) {
    // Base cases
    if (sum == 0) return true;  // A sum of 0 is always possible
    if (n == 0) return false;   // No items left to form the subset

    // If the value is already computed, return it
    if (t[n][sum] != -1) {
        return t[n][sum];
    }

    // Recursive case
    if (arr[n - 1] <= sum) {
        // Include the current element or exclude it
        t[n][sum] = subsetSumTopDownHelper(arr, n - 1, sum - arr[n - 1], t) ||
                       subsetSumTopDownHelper(arr, n - 1, sum, t);
    } else {
        // Exclude the current element
        t[n][sum] = subsetSumTopDownHelper(arr, n - 1, sum, t);
    }

    return t[n][sum];
}

// Top-down DP function to check if the array can be partitioned into subsets with equal sum
bool equalSumPartitionTopDown(int arr[], int n) {
    // Calculate the total sum of the array
    int totalSum = 0;
    for (int i = 0; i < n; i++) {
        totalSum += arr[i];
    }

    // If the total sum is odd, partitioning is not possible
    if (totalSum % 2 != 0) {
        return false;
    }

    // Target sum for each subset
    int targetSum = totalSum / 2;

    // Create a memoization table initialized to -1
    vector<vector<int>> t(n + 1, vector<int>(targetSum + 1, -1));

    // Call the helper function
    return subsetSumTopDownHelper(arr, n, targetSum, t);
}

int main() {
    int arr[] = {1, 5, 11, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    if (equalSumPartitionTopDown(arr, n)) {
        cout << "The array can be partitioned into two subsets with equal sum.\n";
    } else {
        cout << "The array cannot be partitioned into two subsets with equal sum.\n";
    }

    return 0;
}

// top down
int equalPartition(int n, int arr[]){
        int sum=0;
        for(int i=0;i<n;i++) sum+=arr[i];
        if(sum%2!=0 or sum==0) return 0;
         return subset(arr,n,sum/2);
    }
    bool subset(int arr[], int n ,int sum){
        bool t[n+1][sum+1];
        for(int i=0;i<sum+1;i++) t[0][i]=false;
        for(int i=0;i<n+1;i++) t[i][0]=true;
        
        for(int i=1;i<n+1;i++){
            for(int j=1;j<sum+1;j++){
                if(arr[i-1]<=j) t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j];
                else  t[i][j]=t[i-1][j];
            }
        }
    return t[n][sum];
    }    