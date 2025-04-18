#include <iostream>
#include <unordered_map>
using namespace std;

bool willAWinHelper(int n, int x, int y, unordered_map<int, bool>& memo) {
    // Base cases
    if (n == 0) return false; // A loses if no coins left
    if (n == 1) return true;  // A wins if 1 coin is left (can pick the last coin)

    // Check memoization table to avoid recomputation
    if (memo.find(n) != memo.end()) {
        return memo[n];
    }

    // Check all possible moves for A
    // Option 1: Pick 1 coin
    if (n - 1 >= 0 && !willAWinHelper(n - 1, x, y, memo)) {
        return memo[n] = true; // A wins
    }

    // Option 2: Pick x coins
    if (n - x >= 0 && !willAWinHelper(n - x, x, y, memo)) {
        return memo[n] = true; // A wins
    }

    // Option 3: Pick y coins
    if (n - y >= 0 && !willAWinHelper(n - y, x, y, memo)) {
        return memo[n] = true; // A wins
    }

    // If none of the moves lead to a win for A, A loses
    return memo[n] = false;
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
