#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Recursive function to form sentences from the word lists
void solve(int row, int col, string ans, const vector<vector<string>>& matrix) {
    // Base case: If we've processed all rows (word lists), print the sentence
    if (row == matrix.size()) {
        cout << ans << endl; // Print the formed sentence
        return;
    }

    // Loop through each word in the current row
    for (int i = 0; i < col; i++) {
        string word = matrix[row][i]; // Select the word from the current row
        // Recur to process the next row, appending the current word to the answer
        solve(row + 1, col, ans + (ans.empty() ? "" : " ") + word, matrix);
    }
}

// Wrapper function to initiate the recursive process
void generateSentences(const vector<vector<string>>& matrix) {
    if (matrix.empty()) return; // Check for empty matrix
    int colSize = matrix[0].size(); // Get the size of the first row
    solve(0, colSize, "", matrix); // Start solving with row 0
}

int main() {
    // Input: List of word lists
    vector<vector<string>> matrix = {
        {"you", "we"},
        {"have", "are"},
        {"sleep", "eat", "drink"}
    };

    // Call the wrapper function to generate sentences
    generateSentences(matrix);

    return 0;
}


//with backtrack because we passed ans as reference
void solve(int row, int col, string &ans, const vector<vector<string>>& matrix) {
    // Base case: If we've processed all rows (word lists), print the sentence
    if (row == matrix.size()) {
        cout << ans << endl; // Print the formed sentence
        return;
    }

    // Loop through each word in the current row
    for (int i = 0; i < col; i++) {
        string word = matrix[row][i]; // Select the word from the current row

        // Append the current word to the answer
        ans += (ans.empty() ? "" : " ") + word; 
        // Recur to process the next row
        solve(row + 1, col, ans, matrix);
        
        // Backtrack: remove the last added word
        // This is necessary to maintain the correct state of `ans`
        size_t pos = ans.rfind(" "); // Find the last space
        if (pos != string::npos) {
            ans.erase(pos); // Remove the last word
        } else {
            ans.clear(); // If there was no space, clear the string
        }
    }
}