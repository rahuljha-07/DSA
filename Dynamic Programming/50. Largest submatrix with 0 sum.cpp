#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

// Global Memoization Table using an unordered_map
// Key: prefixSum
// Value: pair<rowStart, colIndex>
unordered_map<int, pair<int, int>> memo;

/**
 * Function to find the largest zero-sum subarray in a 1D array using prefix sums.
 * 
 * @param columnSums The input array representing compressed row sums.
 * @param rowStart The starting row of the current submatrix.
 * @return The maximum area of the zero-sum submatrix.
 */
int maxZeroSumSubarray(vector<int>& columnSums, int rowStart) {
    unordered_map<int, int> prefixSumMap;
    prefixSumMap[0] = -1; // To handle the case when prefix sum itself is 0
    int prefixSum = 0, maxLength = 0;

    for (int col = 0; col < columnSums.size(); ++col) {
        prefixSum += columnSums[col];

        if (prefixSumMap.find(prefixSum) != prefixSumMap.end()) {
            int length = col - prefixSumMap[prefixSum];
            maxLength = max(maxLength, length);
            
            // Store the prefix sum with rowStart and column index
            memo[prefixSum] = {rowStart, col};
        } else {
            prefixSumMap[prefixSum] = col;
        }
    }

    return maxLength * (rowStart + 1); // Area = width * height
}

/**
 * Helper function to calculate the maximum area of a submatrix with sum 0
 * starting from a specific row (`rowStart`) using simplified memoization.
 * 
 * @param matrix The input 2D matrix.
 * @param rowStart The starting row for the current submatrix.
 * @return The maximum area of a submatrix with sum 0.
 */
int solve(vector<vector<int>>& matrix, int rowStart) {
    int n = matrix.size();    // Number of rows
    int m = matrix[0].size(); // Number of columns
    int maxArea = 0;

    // Initialize column sums to 0
    vector<int> columnSums(m, 0);

    // Extend the submatrix downwards from rowStart
    for (int rowEnd = rowStart; rowEnd < n; ++rowEnd) {
        // Accumulate column sums
        for (int col = 0; col < m; ++col) {
            columnSums[col] += matrix[rowEnd][col];
        }

        // Calculate the maximum zero-sum subarray area in the current column sums
        maxArea = max(maxArea, maxZeroSumSubarray(columnSums, rowEnd - rowStart + 1));
    }

    return maxArea;
}

/**
 * Main function to find the largest submatrix with sum 0 using simplified memoization.
 * 
 * @param matrix The input 2D matrix.
 * @return The area of the largest submatrix with sum 0.
 */
int largestSubmatrixWithSumZero(vector<vector<int>>& matrix) {
    int n = matrix.size();    // Number of rows
    int maxArea = 0;

    // Clear the global memoization table before starting
    memo.clear();

    // Iterate over each starting row
    for (int rowStart = 0; rowStart < n; ++rowStart) {
        maxArea = max(maxArea, solve(matrix, rowStart));
    }

    return maxArea;
}

// Example usage
int main() {
    vector<vector<int>> matrix = { {0, 0, 1, 1},
                                    {0, 1, 1, 0},
                                    {1, 1, 1, 0},
                                    {1, 0, 0, 1} };
    cout << "Largest Submatrix with Sum 0 Area: " 
         << largestSubmatrixWithSumZero(matrix) << endl;

    return 0;
}

/*
Approach to Find the Largest Submatrix with Sum 0 Using Memoization:

1. Initialize a Global Memoization Table:
   - Use 'unordered_map<int, pair<int, int>> memo' for efficient storage.
   - Key: 'prefixSum' (cumulative sum of column sums).
   - Value: 'pair<int, int>' representing:
       - First: 'rowStart' (Starting row of the submatrix).
       - Second: 'colIndex' (Column index where this prefixSum was first seen).

2. Iterate Through Each Starting Row ('rowStart') in the Matrix:
   - For every 'rowStart', call the 'solve' function to find the maximum area 
     of a submatrix with sum 0 starting at 'rowStart'.

3. The 'solve' Function:
   - Initializes an array 'columnSums' to accumulate column-wise sums.
   - Iterates over all possible 'rowEnd' values to extend the submatrix.
   - Accumulates column sums dynamically for each new row included in the submatrix.

4. Memoization Check:
   - During the column sum accumulation, maintain a running 'prefixSum'.
   - Check if this 'prefixSum' already exists in the 'memo' table:
       - If present, directly compute the potential area using the stored 'rowStart' and 'colIndex'.
       - If not present, store the 'prefixSum' with the current 'rowStart' and 'colIndex' in the 'memo'.

5. Calculate the Largest Zero-Sum Subarray:
   - The 'maxZeroSumSubarray' function uses the prefix sums and the memoized values.
   - Calculates the maximum width of the zero-sum subarray using hashmap lookup.

6. Calculate the Area of the Current Submatrix:
   - Area = (Height of submatrix) * (Width of zero-sum subarray)
   - 'Height' is determined by 'rowEnd - rowStart + 1'.
   - 'Width' is the length of the zero-sum subarray.

7. Update the Maximum Area ('maxArea') Found So Far:
   - Compare the 'currentArea' with 'maxArea' and update accordingly.

8. Continue This Process for Every 'rowStart' and 'rowEnd' Combination:
   - Efficiently handles all possible submatrices using the memoized prefix sums.

9. The 'maxArea' Holds the Area of the Largest Submatrix with Sum 0:
   - The final result is returned as the maximum area found.
*/
