#include <iostream>
#include <vector>
using namespace std;

void displayBoard(vector<vector<int>>& chess) {
    for (int i = 0; i < chess.size(); i++) { // Iterate over rows
        for (int j = 0; j < chess[i].size(); j++) { // Iterate over columns
            cout << chess[i][j] << " "; // Print each cell
        }
        cout << endl; // Move to the next line after each row
    }
    cout << endl; // Extra line for better formatting
}


// Recursive function to find and print all possible knight's tours
void printKnightsTour(vector<vector<int>>& chess, int row, int col, int move) {
    // Boundary conditions: If the knight moves out of bounds or revisits a cell
    if (row < 0 || col < 0 || row >= chess.size() || col >= chess.size() || chess[row][col] != 0) {
        return;
    }

    // If all cells are visited, print the chessboard
    if (move == chess.size() * chess.size()) {
        chess[row][col] = move;  // Mark the last move
        displayBoard(chess);    // Display the complete tour
        chess[row][col] = 0;    // Backtrack
        return;
    }

    // Mark the current cell with the current move number
    chess[row][col] = move;

    // Recursively try all 8 possible knight moves
    printKnightsTour(chess, row - 2, col + 1, move + 1); // Move 1
    printKnightsTour(chess, row - 1, col + 2, move + 1); // Move 2
    printKnightsTour(chess, row + 1, col + 2, move + 1); // Move 3
    printKnightsTour(chess, row + 2, col + 1, move + 1); // Move 4
    printKnightsTour(chess, row + 2, col - 1, move + 1); // Move 5
    printKnightsTour(chess, row + 1, col - 2, move + 1); // Move 6
    printKnightsTour(chess, row - 1, col - 2, move + 1); // Move 7
    printKnightsTour(chess, row - 2, col - 1, move + 1); // Move 8

    // Backtrack: Unmark the current cell
    chess[row][col] = 0;
}

int main() {
    int n; // Size of the chessboard
    int startRow, startCol; // Starting position of the knight

    cout << "Enter the size of the chessboard (n): ";
    cin >> n;
    cout << "Enter the starting row: ";
    cin >> startRow;
    cout << "Enter the starting column: ";
    cin >> startCol;

    // Initialize the chessboard with 0s
    vector<vector<int>> chess(n, vector<int>(n, 0));

    // Start the knight's tour from the given starting position
    printKnightsTour(chess, startRow, startCol, 1);

    return 0;
}
