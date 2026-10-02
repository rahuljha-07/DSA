#include <iostream>
#include <vector>
#include <climits>
using namespace std;

//  your Kadane's algorithm
int maxSubarraySum(vector<int>& arr) {
    int maxi = INT_MIN, sum = 0;
    for (int i = 0; i < (int)arr.size(); i++) {
        sum += arr[i];
        maxi = max(maxi, sum);
        if (sum < 0) sum = 0;
    }
    return maxi;
}

//  same shape as your `solve` from above question
int solve(vector<vector<int>>& matrix, int rowStart) {
    int n = matrix.size();        // rows
    int m = matrix[0].size();     // cols
    int maxSum = INT_MIN;

    // columnwise running sums for the band [rowStart..rowEnd]
    vector<int> columnSums(m, 0);

    // Extend the submatrix downward from rowStart
    for (int rowEnd = rowStart; rowEnd < n; ++rowEnd) {
        // Accumulate column sums
        for (int col = 0; col < m; ++col) {
            columnSums[col] += matrix[rowEnd][col];
        }

        // For the current band, best rectangle = Kadane on columnSums
        int bestHere = maxSubarraySum(columnSums);
        maxSum = max(maxSum, bestHere);
    }

    return maxSum;
}

//  outer driver (same loop pattern) 
int maximumSumRectangle(vector<vector<int>>& matrix) {
    int n = matrix.size();
    int ans = INT_MIN;
    for (int rowStart = 0; rowStart < n; ++rowStart) {
        ans = max(ans, solve(matrix, rowStart));
    }
    return ans;
}

//  example 
int main() {
    vector<vector<int>> mat = {
        { 1,  2, 1,  4, 20},
        {8, 3,  4,  2,   1},
        { 3,  8, 10,  1,   3},
        {4, 1,  1,  7,  6}
    };
    cout << "Maximum Sum Rectangle: "
         << maximumSumRectangle(mat) << endl; // expected 29
    return 0;
}
