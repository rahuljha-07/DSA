#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxSteal(const vector<int>& houses, int index, vector<int>& memo) {
    // Base case: if no houses are left, return 0
    if (index >= houses.size()) {
        return 0;
    }

    // Check if we've already computed the result for this index
    if (memo[index] != -1) {
        return memo[index];
    }

    // Option 1: Steal from the current house and skip the next one
    int steal = houses[index] + maxSteal(houses, index + 2, memo);

    // Option 2: Skip the current house and move to the next one
    int skip = maxSteal(houses, index + 1, memo);

    // Store the result in memo and return the maximum of both choices
    memo[index] = max(steal, skip);
    return memo[index];
}

int main() {
    vector<int> houses = {6, 7, 1, 30, 8, 2, 4};  // Example house values
    vector<int> memo(houses.size(), -1);  // Initialize memoization vector with -1
    int result = maxSteal(houses, 0, memo);
    cout << "Maximum money that can be stolen: " << result << endl;
    return 0;
}
