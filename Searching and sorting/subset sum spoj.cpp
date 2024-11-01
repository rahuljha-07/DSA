#include <iostream>
#include <vector>

using namespace std;

// Recursive function to count subsets
void countSubsets(int index, int currentSum, const vector<int>& nums, int A, int B, int& count) {
    // Base case: if we've processed all elements
    if (index == nums.size()) {
        // Check if the current sum is within the range [A, B]
        if (currentSum >= A && currentSum <= B) {
            count++; // Increment count if within range
        }
        return;
    }

    // Include the current element in the subset
    countSubsets(index + 1, currentSum + nums[index], nums, A, B, count);

    // Exclude the current element from the subset
    countSubsets(index + 1, currentSum, nums, A, B, count);
}

int main() {
    int N, A, B;
    cin >> N >> A >> B;
    
    vector<int> nums(N);
    for (int i = 0; i < N; i++) {
        cin >> nums[i];
    }

    int count = 0; // To count the valid subsets
    countSubsets(0, 0, nums, A, B, count); // Start recursion

    cout << count << endl; // Output the count of valid subsets
    return 0;
}
