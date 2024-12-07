#include <iostream>
#include <unordered_map>
using namespace std;

// Function to determine if A will win with given n coins
bool willAWinHelper(int n, int x, int y, unordered_map<int, bool>& memo) {
    // Base cases
    if (n == 0) return false; // A loses if no coins are left
    if (n == 1) return true;  // A wins if there's only 1 coin

    // Check if the result for n is already computed
    if (memo.find(n) != memo.end()) {
        return memo[n];
    }

    // Check if A can force B into a losing position
    bool pick1 = (n - 1 >= 0 && !willAWinHelper(n - 1, x, y, memo)); // Pick 1 coin
    bool pickX = (n - x >= 0 && !willAWinHelper(n - x, x, y, memo)); // Pick x coins
    bool pickY = (n - y >= 0 && !willAWinHelper(n - y, x, y, memo)); // Pick y coins

    // A wins if any of the above moves force B into a losing position
    memo[n] = pick1 || pickX || pickY;

    // Return the result for the current state
    return memo[n];
}

// Wrapper function to initialize memoization and call the recursive helper
bool willAWin(int n, int x, int y) {
    unordered_map<int, bool> memo; // Memoization table
    return willAWinHelper(n, x, y, memo);
}

// Main function to test the solution
int main() {
    int n = 5, x = 3, y = 4;
    if (willAWin(n, x, y)) {
        cout << "A" << endl; // A wins
    } else {
        cout << "B" << endl; // B wins
    }
    return 0;
}
