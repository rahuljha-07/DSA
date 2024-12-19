int rowWithMax1s(vector<vector<int>> arr) {
        int n = arr.size();          // Get number of rows
        int m = arr[0].size();       // Get number of columns
        int maxRowIndex = -1;        // Initialize to -1 to indicate no row found
        int i = 0;                   // Start from the first row
        int j = m - 1;               // Start from the last column

        // Traverse the matrix from the top-right corner
        while (i < n && j >= 0) {
            if (arr[i][j] == 1) {
                // Update the index of the row with maximum 1s
                maxRowIndex = i;
                j--; // Move left
            } else {
                i++; // Move down
            }
        }

        // Return the row index with the maximum number of 1s found
        return maxRowIndex;
    }
// traversing from arr[0][m] and if its 1 then move left and 0 then move bottom