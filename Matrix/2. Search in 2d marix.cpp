#include <vector>
using namespace std;

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int m = matrix.size();       // Number of rows in the matrix
    int n = matrix[0].size();    // Number of columns in the matrix
    int low = 0, high = m * n - 1; // Set search range for the virtual 1D array

    // Binary search on the virtual 1D array
    while (low <= high) {
        int mid = (low + high) / 2; // Middle index in the virtual 1D array
        int row = mid / n;          // Row index in the 2D matrix
        int col = mid % n;          // Column index in the 2D matrix

        if (matrix[row][col] == target) {
            return true; // Target found
        } else if (matrix[row][col] < target) {
            low = mid + 1; // Move to the right half
        } else {
            high = mid - 1; // Move to the left half
        }
    }

    return false; // Target not found
}

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int rows = matrix.size();
    int cols = matrix[0].size();
    
    // Start from the top-right corner
    int row = 0, col = cols - 1;

    while (row < rows && col >= 0) {
        if (matrix[row][col] == target) {
            return true; // Target found
        } else if (matrix[row][col] > target) {
            col--; // Move left
        } else {
            row++; // Move down
        }
    }

    return false; // Target not found
}