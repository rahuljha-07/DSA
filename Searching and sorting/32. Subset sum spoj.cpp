#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

// Memoization map: key = "index_sum", value = number of valid subsets
unordered_map<string, int> memo;

int countSubsets(int index, int currentSum, const vector<int>& nums, int A, int B) {
    // Base case
    if (index == nums.size()) {
        return (currentSum >= A && currentSum <= B) ? 1 : 0;
    }

    // Generate a unique key for memoization
    string key = to_string(index) + "_" + to_string(currentSum);

    // Check if result is already memoized
    if (memo.find(key) != memo.end()) {
        return memo[key];
    }

    // Include current element
    int include = countSubsets(index + 1, currentSum + nums[index], nums, A, B);

    // Exclude current element
    int exclude = countSubsets(index + 1, currentSum, nums, A, B);

    // Memoize and return
    return memo[key] = include + exclude;
}

int main() {
    int N, A, B;
    cin >> N >> A >> B;

    vector<int> nums(N);
    for (int i = 0; i < N; i++) {
        cin >> nums[i];
    }

    int totalCount = countSubsets(0, 0, nums, A, B);

    cout << totalCount << endl;
    return 0;
}
