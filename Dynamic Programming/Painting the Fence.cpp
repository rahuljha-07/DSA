#include <iostream>
#include <vector>
using namespace std;

/*
   Function to calculate the number of ways to paint the fence with constraints:
   - No more than two consecutive posts can have the same color.

   Global DP table `t` is used for memoization:
   - `t[i]` stores the number of ways to paint a fence with `i` posts and `k` colors.
   - If `t[i]` is not -1, it means the result for `i` posts has already been computed.
*/

vector<int> t; // Global memoization table

int paintFence(int n, int k) {
    // Base cases
    if (n == 1) return k;          // One post, k ways to paint it
    if (n == 2) return k * k;      // Two posts, each can independently be painted with k colors

    // If result is already computed, return it
    if (t[n] != -1) return t[n];

    // Recursive relation
    t[n] = (k - 1) * (paintFence(n - 1, k) + paintFence(n - 2, k));
    return t[n];
}

int main() {
    int n = 3, k = 2; // Example input: 3 posts and 2 colors

    // Initialize the memoization table with -1
    t.assign(n + 1, -1);

    cout << "Number of ways to paint the fence with " << n << " posts and " << k << " colors: "
         << paintFence(n, k) << endl;

    n = 4, k = 3; // Another example input: 4 posts and 3 colors
    t.assign(n + 1, -1); // Reset the memoization table for the new input
    cout << "Number of ways to paint the fence with " << n << " posts and " << k << " colors: "
         << paintFence(n, k) << endl;

    return 0;
}
