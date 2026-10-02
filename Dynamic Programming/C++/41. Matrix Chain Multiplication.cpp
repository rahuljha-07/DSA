#include <iostream>
#include <vector>
#include <climits>
using namespace std;

/**
 * Function to solve the Matrix Chain Multiplication problem using recursion with memoization.
 * 
 * Explanation:
 * - MCM calculates the minimum cost (number of scalar multiplications) to multiply a chain of matrices.
 * - The cost to multiply matrices A[i] x A[i+1] ... x A[j] depends on where we place the parenthesis.
 * - For every possible split point `k` between `i` and `j`, calculate:
 *   - Cost to multiply matrices from `i` to `k`.
 *   - Cost to multiply matrices from `k+1` to `j`.
 *   - Cost to combine the results of the two subproblems.
 * - Use memoization to avoid redundant calculations.
 * 
 * Time Complexity: O(n^3) (n is the number of matrices)
 * Space Complexity: O(n^2) (for memoization table)
 */

// Define a memoization table
vector<vector<int>> t;

// Recursive function to solve MCM
int solve(vector<int>& arr, int i, int j) {
    // Base case: If the chain has less than two matrices, no cost
    if (i >= j) return 0;

    // Check if the result is already computed in the memoization table
    if (t[i][j] != -1) return t[i][j];

    int ans = INT_MAX; // Initialize the minimum cost to a large value

    // Try placing the parenthesis at every possible split point `k`
    for (int k = i; k < j; k++) {
        // Cost of multiplying matrices from i to k and k+1 to j
        int temp = solve(arr, i, k) + solve(arr, k + 1, j) + arr[i - 1] * arr[k] * arr[j];

        // Update the minimum cost
        ans = min(ans, temp);
    }

    // Store the result in the memoization table and return it
    return t[i][j] = ans;
}

int main() {
    // Example input: dimensions of matrices
    vector<int> arr = {40, 20, 30, 10, 30};

    int n = arr.size();

    // Initialize the memoization table with -1
    t.assign(n, vector<int>(n, -1));

    // Solve the MCM problem
    int result = solve(arr, 1, n - 1);

    // Output the result
    cout << "Minimum number of multiplications is: " << result << endl;

    return 0;
}
