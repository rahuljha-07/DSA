#include <bits/stdc++.h>
using namespace std;

// Function to build the prefix table for KMP algorithm
vector<int> buildPrefixTable(const string& pattern) {
    int m = pattern.size();
    vector<int> prefixTable(m, 0);
    int j = 0; // Length of the previous longest prefix suffix

    for (int i = 1; i < m; i++) {
        while (j > 0 && pattern[i] != pattern[j]) {
            j = prefixTable[j - 1];
        }
        if (pattern[i] == pattern[j]) {
            j++;
        }
        prefixTable[i] = j;
    }
    return prefixTable;
}

// KMP search algorithm
int kmpSearch(const string& text, const string& pattern) {
    vector<int> prefixTable = buildPrefixTable(pattern);
    int count = 0;
    int j = 0; // Index for pattern

    for (int i = 0; i < text.size(); i++) {
        while (j > 0 && text[i] != pattern[j]) {
            j = prefixTable[j - 1];
        }
        if (text[i] == pattern[j]) {
            j++;
        }
        if (j == pattern.size()) {
            count++; // Found an occurrence
            j = prefixTable[j - 1]; // Reset j for the next potential match
        }
    }
    return count;
}

// Function to search for the pattern in all directions in the 2D array
int countOccurrences(const vector<vector<char>>& grid, const string& str) {
    int rows = grid.size();
    int cols = grid[0].size();
    string pattern(str);
    int totalCount = 0;

    // Search horizontally (left to right and right to left)
    for (int i = 0; i < rows; i++) {
        string rowText(cols, ' ');
        for (int j = 0; j < cols; j++) {
            rowText[j] = grid[i][j];
        }
        totalCount += kmpSearch(rowText, pattern); // Left to right
        reverse(rowText.begin(), rowText.end());
        totalCount += kmpSearch(rowText, pattern); // Right to left
    }

    // Search vertically (top to down and down to top)
    for (int j = 0; j < cols; j++) {
        string colText(rows, ' ');
        for (int i = 0; i < rows; i++) {
            colText[i] = grid[i][j];
        }
        totalCount += kmpSearch(colText, pattern); // Top to down
        reverse(colText.begin(), colText.end());
        totalCount += kmpSearch(colText, pattern); // Down to top
    }

    return totalCount;
}

int main() {
    vector<vector<char>> grid1 = {
        {'D', 'D', 'D', 'G', 'D', 'D'},
        {'B', 'B', 'D', 'E', 'B', 'S'},
        {'B', 'S', 'K', 'E', 'B', 'K'},
        {'D', 'D', 'D', 'D', 'D', 'E'},
        {'D', 'D', 'D', 'D', 'D', 'E'},
        {'D', 'D', 'D', 'D', 'D', 'G'}
    };
    string str1 = "GEEKS";
    cout << "Output for grid1: " << countOccurrences(grid1, str1) << endl; // Output: 1

    vector<vector<char>> grid2 = {
        {'B', 'B', 'M', 'B', 'B', 'B'},
        {'C', 'B', 'A', 'B', 'B', 'B'},
        {'I', 'B', 'G', 'B', 'B', 'B'},
        {'G', 'B', 'I', 'B', 'B', 'B'},
        {'A', 'B', 'C', 'B', 'B', 'B'},
        {'M', 'C', 'I', 'G', 'A', 'M'}
    };
    string str2 = "MAGIC";
    cout << "Output for grid2: " << countOccurrences(grid2, str2) << endl; // Output: 3

    return 0;
}


// recursive
// Directions for moving in the matrix
int dx[] = {0, 0, -1, 1}; // left, right, up, down
int dy[] = {-1, 1, 0, 0};

// Helper function for recursive search
int searchFromCell(const vector<vector<char>>& grid, const string& pattern, int x, int y, int index) {
    int rows = grid.size();
    int cols = grid[0].size();

    // Base cases
    if (index == pattern.size()) return 1; // Found the pattern
    if (x < 0 || y < 0 || x >= rows || y >= cols || grid[x][y] != pattern[index]) return 0;

    // Mark the current cell as visited to prevent revisiting
    char temp = grid[x][y];
    grid[x][y] = '#'; // Temporarily mark as visited

    int count = 0;
    // Explore all 4 directions
    for (int dir = 0; dir < 4; dir++) {
        int newX = x + dx[dir];
        int newY = y + dy[dir];
        count += searchFromCell(grid, pattern, newX, newY, index + 1);
    }

    // Restore the original value of the cell
    grid[x][y] = temp;

    return count;
}

// Main function to count pattern occurrences in the grid
int countOccurrencesInGrid(const vector<vector<char>>& grid, const string& pattern) {
    int rows = grid.size();
    int cols = grid[0].size();
    int totalCount = 0;

    // Iterate through every cell in the matrix
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            // Start recursion if the first character matches
            if (grid[i][j] == pattern[0]) {
                totalCount += searchFromCell(grid, pattern, i, j, 0);
            }
        }
    }

    return totalCount;
}