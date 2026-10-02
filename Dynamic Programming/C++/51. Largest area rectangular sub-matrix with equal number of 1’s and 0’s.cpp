/*
Same as largest submatrix with 0 sum.
There was a array question why says find largest equal 0 and 1
So we replace 0->-1 and 1-> 1 
and do the same below is sample
*/

int maxLengthEqual01(vector<int>& nums) {
    unordered_map<int, int> prefixSumMap;
    prefixSumMap[0] = -1; // Initialize to handle the case when the array starts with a balanced subarray

    int prefixSum = 0;
    int maxLength = 0;

    for (int i = 0; i < nums.size(); ++i) {
        // Transform 0 to -1 to balance with 1s
        prefixSum += (nums[i] == 0) ? -1 : 1;

        // Check if the prefix sum has been seen before
        if (prefixSumMap.find(prefixSum) != prefixSumMap.end()) {
            // Calculate the length of the balanced subarray
            maxLength = max(maxLength, i - prefixSumMap[prefixSum]);
        } else {
            // Store the first occurrence of the prefix sum
            prefixSumMap[prefixSum] = i;
        }
    }

    return maxLength;
};


// now the complete code
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int maxZeroSumSubarray(vector<int>& columnSums) {
    unordered_map<int, int> prefixSumMap;
    prefixSumMap[0] = -1; // To handle the case when prefix sum itself is 0
    int prefixSum = 0, maxLength = 0;

    for (int col = 0; col < columnSums.size(); ++col) {
        prefixSum += columnSums[col];

        if (prefixSumMap.find(prefixSum) != prefixSumMap.end()) {
            int length = col - prefixSumMap[prefixSum];
            maxLength = max(maxLength, length);
        } else {
            prefixSumMap[prefixSum] = col;
        }
    }

    return maxLength;
}


int solve(vector<vector<int>>& matrix, int rowStart) {
    int n = matrix.size();    // Number of rows
    int m = matrix[0].size(); // Number of columns
    int maxArea = 0;

    // Initialize column sums to 0
    vector<int> columnSums(m, 0);

    // Extend the submatrix downwards from rowStart
    for (int rowEnd = rowStart; rowEnd < n; ++rowEnd) {
        // Accumulate column sums with transformed values (0 -> -1, 1 -> 1)
        for (int col = 0; col < m; ++col) {
            columnSums[col] += (matrix[rowEnd][col] == 0 ? -1 : 1);
        }

        // Calculate the maximum zero-sum subarray length in the current column sums
        int maxWidth = maxZeroSumSubarray(columnSums);

        // Calculate the area of the current submatrix
        int height = rowEnd - rowStart + 1;
        int currentArea = maxWidth * height;

        // Update the maximum area found
        maxArea = max(maxArea, currentArea);
    }

    return maxArea;
}

int largestSubmatrixWithEqual01(vector<vector<int>>& matrix) {
    int n = matrix.size();    // Number of rows
    int maxArea = 0;

    // Iterate over each starting row
    for (int rowStart = 0; rowStart < n; ++rowStart) {
        // Call the solve function for each rowStart
        maxArea = max(maxArea, solve(matrix, rowStart));
    }

    return maxArea;
}

// Example usage
int main() {
    vector<vector<int>> matrix = {
        {0, 0, 1, 1},
        {0, 1, 1, 0},
        {1, 1, 1, 0},
        {1, 0, 0, 1}
    };
    cout << "Largest Submatrix with Equal 0's and 1's Area: " 
         << largestSubmatrixWithEqual01(matrix) << " sq. units" << endl;

    return 0;
}
