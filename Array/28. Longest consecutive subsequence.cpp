#include <iostream>
#include <unordered_set>
#include <climits>
using namespace std;

int findLongestConseqSubseq(int arr[], int n) {
    unordered_set<int> s; // Set to store unique elements
    int maxi = INT_MIN;   // Track the maximum element in the array
    int mini = INT_MAX;   // Track the minimum element in the array

    // Insert elements into the set and find min and max
    for (int i = 0; i < n; i++) {
        maxi = max(maxi, arr[i]);
        mini = min(mini, arr[i]);
        s.insert(arr[i]);
    }

    int count = 0, ans = 0;

    // Iterate through the range from mini to maxi
    for (int i = mini; i <= maxi; i++) {
        if (s.find(i) != s.end()) {
            count++; // Increment count for consecutive numbers
        } else {
            ans = max(ans, count); // Update the longest sequence length
            count = 0;             // Reset count for a new sequence
        }
    }

    // Update the answer with the final sequence count
    ans = max(ans, count);
    return ans;
}

int main() {
    int arr[] = {1, 9, 3, 10, 4, 20, 2}; // Example input
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Length of the longest consecutive subsequence is: "
         << findLongestConseqSubseq(arr, n) << endl;

    return 0;
}
