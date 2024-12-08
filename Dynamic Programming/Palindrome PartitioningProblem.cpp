#include <iostream>
#include <vector>
#include <string>
#include <climits>
using namespace std;

// Global memoization table
vector<vector<int>> t;

/**
 * Helper function to check if a substring str[i..j] is a palindrome.
 * 
 * Time Complexity: O(j - i) for each call (linear check of the substring).
 */
bool isPalindrome(const string& str, int i, int j) {
    while (i < j) {
        if (str[i] != str[j]) return false;
        i++;
        j--;
    }
    return true;
}

/**
 * Recursive function to solve the Palindrome Partitioning problem.
 * 
 * Steps:
 * 1. Base Case:
 *    - If i >= j, no cuts are needed.
 *    - If str[i..j] is a palindrome, no cuts are needed.
 * 2. Recursive Case:
 *    - Try all possible partitions and calculate the minimum cuts needed.
 *    - Check the memoization table (`t`) before making recursive calls to avoid redundant computations.
 * 3. Memoization:
 *    - Use the global 2D table `t` to store results of subproblems.
 * 
 * Time Complexity: O(n^3) (due to palindrome check and recursion).
 * Space Complexity: O(n^2) (for memoization table).
 */
int solve(const string& str, int i, int j) {
    // Base case: If the substring length is 1 or less, no cuts are needed
    if (i >= j) return 0;

    // If the substring is already a palindrome, no cuts are needed
    if (isPalindrome(str, i, j)) return 0;

    // Check if the result is already computed
    if (t[i][j] != -1) return t[i][j];

    int ans = INT_MAX; // Initialize the minimum cuts to a large value

    // Try all possible partitions
    for (int k = i; k < j; k++) {
        // Avoid redundant recursive calls by checking the memoization table
        int left = (t[i][k] != -1) ? t[i][k] : solve(str, i, k);
        int right = (t[k + 1][j] != -1) ? t[k + 1][j] : solve(str, k + 1, j);

        // Calculate the number of cuts recursively
        int temp = left + right + 1;

        // Update the minimum cuts
        ans = min(ans, temp);
    }

    // Store the result in the memoization table
    return t[i][j] = ans;
}

int main() {
    string str = "ababbbabbababa"; // Example input

    int n = str.length();

    // Resize and initialize the global memoization table with -1
    t.resize(n, vector<int>(n, -1));

    // Solve the Palindrome Partitioning problem
    int result = solve(str, 0, n - 1);

    // Output the result
    cout << "Minimum number of cuts needed for Palindrome Partitioning is: " << result << endl;

    return 0;
}
