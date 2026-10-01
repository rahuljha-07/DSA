#include <bits/stdc++.h>
using namespace std;

// Function to find the maximum difference between any element and a smaller element
// that appears before it in the matrix.
int maxDiff(vector<vector<int>>& matrix, int n) {
    // Create a 2D vector to store the maximum values in the matrix from each position
    vector<vector<int>> maxMat(n, vector<int>(n));

    // Initialize the bottom-right element as itself since it's the last element
    maxMat[n - 1][n - 1] = matrix[n - 1][n - 1];

    // Fill the last row with maximum values from the current position to the right
    for (int j = n - 2; j >= 0; j--) {
        maxMat[n - 1][j] = max(matrix[n - 1][j], maxMat[n - 1][j + 1]);
    }

    // Fill the last column with maximum values from the current position downward
    for (int i = n - 2; i >= 0; i--) {
        maxMat[i][n - 1] = max(matrix[i][n - 1], maxMat[i + 1][n - 1]);
    }

    // Fill the rest of maxMat with the maximum value seen from each position
    for (int i = n - 2; i >= 0; i--) {
        for (int j = n - 2; j >= 0; j--) {
            maxMat[i][j] = max({maxMat[i + 1][j], maxMat[i][j + 1], matrix[i][j]});
        }
    }

    // Find the maximum difference between maxMat and the original matrix
    int ans = INT_MIN;
    for (int a = 0; a < n - 1; a++) {
        for (int b = 0; b < n - 1; b++) {
            ans = max(ans, maxMat[a + 1][b + 1] - matrix[a][b]);
        }
    }

    return ans;
}

// Function to read matrix input and calculate the maximum difference
void solve() {
    int n;
    cin >> n;

    vector<vector<int>> matrix(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }

    cout << "MAX VALUE IS: " << maxDiff(matrix, n) << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int tc = 1; // Number of test cases (fixed to 1 in this example)
    while (tc--) {
        solve();
    }
    return 0;
}

// fill the last row , col for the base case/starting