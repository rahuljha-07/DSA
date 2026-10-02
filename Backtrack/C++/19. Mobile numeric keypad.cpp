#include <iostream>
#include <vector>
using namespace std;

// Function to check if a move is valid (i.e., within bounds of the keypad matrix)
bool isValid(int row, int col) {
    return (row >= 0 && row < 4 && col >= 0 && col < 3 && !(row == 3 && (col == 0 || col == 2)));  // Skip * and #
}

// Recursive function to generate all possible sequences
void generateSequences(int row, int col, int n, string &current, vector<vector<int>> &keypad, vector<string> &result) {
    // Base case: If length of the current sequence is n, add it to result
    if (n == 0) {
        result.push_back(current);
        return;
    }

    // Explore all 5 possible directions: left, right, up, down, and stay at the same position
    int moves[5][2] = {{0, 0}, {1, 0}, {-1, 0}, {0, 1}, {0, -1}};  // stay, down, up, right, left

    for (int i = 0; i < 5; i++) {
        int newRow = row + moves[i][0];
        int newCol = col + moves[i][1];

        // Ensure the move is valid
        if (isValid(newRow, newCol)) {
            // Append the new digit to the sequence
            current.push_back(char('0' + keypad[newRow][newCol]));
            // Recurse for the next digit
            generateSequences(newRow, newCol, n - 1, current, keypad, result);
            // Backtrack and remove the last digit added
            current.pop_back();
        }
    }
}

int main() {
    // Define the keypad as a matrix
    vector<vector<int>> keypad = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9},
        {10, 0, 11} // Using 10 for * and 11 for # to simplify
    };

    int n;
    cout << "Enter the length of the sequence (n): ";
    cin >> n;

    vector<string> result;

    // Generate sequences starting from each key (0 to 9)
    for (int row = 0; row < 4; row++) {
        for (int col = 0; col < 3; col++) {
            if (keypad[row][col] != 10 && keypad[row][col] != 11) { // Avoid * and #
                string current = "";
                current.push_back(char('0' + keypad[row][col]));
                generateSequences(row, col, n - 1, current, keypad, result);
            }
        }
    }

    // Output the total number of sequences generated
    cout << "Total number of sequences of length " << n << ": " << result.size() << endl;
    for (const string &seq : result) {
        cout << seq << endl;
    }

    return 0;
}