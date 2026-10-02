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
        // Accumulate column sums
        for (int col = 0; col < m; ++col) {
            columnSums[col] += matrix[rowEnd][col];
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

int largestSubmatrixWithSumZero(vector<vector<int>>& matrix) {
    int n = matrix.size();    // Number of rows
    int maxArea = 0;

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
