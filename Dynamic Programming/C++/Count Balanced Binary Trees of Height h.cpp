#include <iostream>
using namespace std;

// Recursive function to count the number of balanced binary trees of height h
int countBBT(int h) {
    // Base cases:
    if (h == 0) return 1; // An empty tree is balanced
    if (h == 1) return 1; // A single-node tree is balanced

    // Recursive calls:
    // Count of trees of height h-1
    int samelevel = countBBT(h - 1);

    // Count of trees of height h-2
    int difflevel = countBBT(h - 2);

    // Total number of trees for height h:
    // - Case 1: Both subtrees are of height h-1 => samelevel * samelevel
    // - Case 2: One subtree of height h-1 and the other of height h-2 => 2 * samelevel * difflevel
    return samelevel * samelevel + 2 * samelevel * difflevel;
}

int main() {
    int h;
    cin >> h;
    cout << countBBT(h) << endl;
    return 0;
}
