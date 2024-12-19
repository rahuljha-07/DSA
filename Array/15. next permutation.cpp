#include <vector>
#include <algorithm>
using namespace std;

void nextPermutation(vector<int>& nums) {
    int n = nums.size(), k, l;

    // Step 1: Find the largest index `k` such that nums[k] < nums[k + 1]
    for (k = n - 2; k >= 0; k--) {
        if (nums[k] < nums[k + 1]) {
            break;
        }
    }

    // Step 2: If no such index exists, reverse the array (last permutation)
    if (k < 0) {
        reverse(nums.begin(), nums.end());
    } else {
        // Step 3: Find the largest index `l` greater than `k` such that nums[l] > nums[k]
        for (l = n - 1; l > k; l--) {
            if (nums[l] > nums[k]) {
                break;
            }
        }
        // Step 4: Swap nums[k] and nums[l]
        swap(nums[k], nums[l]);

        // Step 5: Reverse the subarray nums[k + 1] to nums[n - 1]
        reverse(nums.begin() + k + 1, nums.end());
    }
}
