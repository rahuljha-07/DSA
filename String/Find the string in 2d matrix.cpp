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

// KMP search algorithm to find occurrences and their starting coordinates
vector<pair<int, int>> kmpSearch(const string& text, const string& pattern, int row, int col) {
    vector<int> prefixTable = buildPrefixTable(pattern);
    vector<pair<int, int>> coordinates;
    int j = 0; // Index for pattern

    for (int i = 0; i < text.size(); i++) {
        while (j > 0 && text[i] != pattern[j]) {
            j = prefixTable[j - 1];
        }
        if (text[i] == pattern[j]) {
            j++;
        }
        if (j == pattern.size()) {
            coordinates.push_back({row, col + i - j + 1}); // Store the starting coordinate
            j = prefixTable[j - 1]; // Reset j for the next potential match
        }
    }
    return coordinates;
}

// Function to search for the pattern in all directions in the 2D array
vector<pair<int, int>> findOccurrences(const vector<vector<char>>& grid, const string& str) {
    int rows = grid.size();
    int cols = grid[0].size();
    string pattern(str);
    vector<pair<int, int>> result;

    // Search horizontally (left to right and right to left)
    for (int i = 0; i < rows; i++) {
        string rowText(cols, ' ');
        for (int j = 0; j < cols; j++) {
            rowText[j] = grid[i][j];
        }
        auto coords = kmpSearch(rowText, pattern, i, 0); // Left to right
        result.insert(result.end(), coords.begin(), coords.end());
        
        reverse(rowText.begin(), rowText.end());
        coords = kmpSearch(rowText, pattern, i, cols - 1); // Right to left
        result.insert(result.end(), coords.begin(), coords.end());
    }

    // Search vertically (top to down and down to top)
    for (int j = 0; j < cols; j++) {
        string colText(rows, ' ');
        for (int i = 0; i < rows; i++) {
            colText[i] = grid[i][j];
        }
        auto coords = kmpSearch(colText, pattern, 0, j); // Top to down
        result.insert(result.end(), coords.begin(), coords.end());
        
        reverse(colText.begin(), colText.end());
        coords = kmpSearch(colText, pattern, rows - 1, j); // Down to top
        result.insert(result.end(), coords.begin(), coords.end());
    }

    // Search diagonally (down-right, down-left, up-right, up-left)
    // Down-right diagonal
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            string diagText;
            int x = i, y = j;
            while (x < rows && y < cols) {
                diagText += grid[x][y];
                x++; y++;
            }
            auto coords = kmpSearch(diagText, pattern, i, j);
            result.insert(result.end(), coords.begin(), coords.end());
        }
    }
    
    // Down-left diagonal
    for (int i = 0; i < rows; i++) {
        for (int j = cols - 1; j >= 0; j--) {
            string diagText;
            int x = i, y = j;
            while (x < rows && y >= 0) {
                diagText += grid[x][y];
                x++; y--;
            }
            auto coords = kmpSearch(diagText, pattern, i, j);
            result.insert(result.end(), coords.begin(), coords.end());
        }
    }
    
    // Up-right diagonal
    for (int i = rows - 1; i >= 0; i--) {
        for (int j = 0; j < cols; j++) {
            string diagText;
            int x = i, y = j;
            while (x >= 0 && y < cols) {
                diagText += grid[x][y];
                x--; y++;
            }
            auto coords = kmpSearch(diagText, pattern, i, j);
            result.insert(result.end(), coords.begin(), coords.end());
        }
    }
    
    // Up-left diagonal
    for (int i = rows - 1; i >= 0; i--) {
        for (int j = cols - 1; j >= 0; j--) {
            string diagText;
            int x = i, y = j;
            while (x >= 0 && y >= 0) {
                diagText += grid[x][y];
                x--; y--;
            }
            auto coords = kmpSearch(diagText, pattern, i, j);
            result.insert(result.end(), coords.begin(), coords.end());
        }
    }

    return result;
}

int main() {
    vector<vector<char>> grid = {
        {'a', 'b', 'a', 'b'},
        {'a', 'b', 'e', 'b'},
        {'e', 'b', 'e', 'b'}
    };
    string word = "abe";
    
    vector<pair<int, int>> occurrences = findOccurrences(grid, word);
    
    cout << "Occurrences of '" << word << "':" << endl;
    for (const auto& coord : occurrences) {
        cout << "{" << coord.first << ", " << coord.second << "}" << endl;
    }

    return 0;
}
