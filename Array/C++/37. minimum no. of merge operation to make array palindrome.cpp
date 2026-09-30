#include <iostream>
#include <vector>
using namespace std;

int findMinOps(vector<int> arr) {
    int ans = 0;               // Count of merge operations
    int n = arr.size();        // Size of the array
    int i = 0, j = n - 1;      // Pointers for the two ends of the array

    // Use two pointers to process the array
    while (i <= j) {
        // If elements at both ends are equal, move both pointers inward
        if (arr[i] == arr[j]) {
            i++;
            j--;
        } 
        // If the left element is greater, merge two elements on the right
        else if (arr[i] > arr[j]) {
            j--;                // Move the right pointer inward
            arr[j] += arr[j + 1]; // Merge arr[j] and arr[j+1]
            ans++;              // Increment the operation count
        } 
        // If the right element is greater, merge two elements on the left
        else {
            i++;                // Move the left pointer inward
            arr[i] += arr[i - 1]; // Merge arr[i] and arr[i-1]
            ans++;              // Increment the operation count
        }
    }

    return ans;
}

int main() {
    vector<int> arr = {1, 4, 5, 1}; // Example input
    cout << "Minimum operations to make the array palindrome: " 
         << findMinOps(arr) << endl;
    return 0;
}
