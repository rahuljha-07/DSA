#include <iostream>
#include <vector>
using namespace std;

// Helper function for recursive backtracking
void countSubsequences(int idx, int product, int k, vector<int> &arr, int &count) {
    // Base case: If product exceeds k, stop recursion
    if (product > k) return;

    // Count the current subsequence (valid since product <= k)
    if (idx == arr.size()) {
        count++;
        return;
    }

    // Include the current element
    countSubsequences(idx + 1, product * arr[idx], k, arr, count);

    // Exclude the current element
    countSubsequences(idx + 1, product, k, arr, count);
}

// Main function
int countSubsequencesWithProductLessThanK(vector<int> &arr, int k) {
    int count = 0;
    countSubsequences(0, 1, k, arr, count);
    return count - 1; // Subtract 1 to exclude the empty subsequence
}

int main() {
    vector<int> arr = {1, 2, 3, 4};
    int k = 10;
    cout << "Number of subsequences with product <= " << k << ": "
         << countSubsequencesWithProductLessThanK(arr, k) << endl;
    return 0;
}
