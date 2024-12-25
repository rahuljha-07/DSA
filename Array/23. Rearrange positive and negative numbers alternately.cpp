// O(n) space uneven +,- ordder maintained
 vector<int> rearrangeWithExtraSpace(const vector<int>& num) {
     vector<int> positives, negatives;
     vector<int> result;

    for (int num : nums) {
        if (num >= 0) positives.push_back(num);
        else negatives.push_back(num);
    }

    int i = 0, j = 0, k = 0;
    while (i < positives.size() && j < negatives.size()) {
        result[k++] = positives[i++];
        result[k++] = negatives[j++];
    }

    // Append remaining elements
    while (i < positives.size()) result[k++] = positives[i++];
    while (j < negatives.size()) result[k++] = negatives[j++];
    return result;
}

// O(1) space uneven +,- order not maintained
void rearrangeInPlace(vector<int>& nums) {
    int pos = 0; // Start with the even index, expecting positive number here
    int neg = 1; // Start with the odd index, expecting negative number here

    while (true) {
        // Step 1: Find the first misplaced positive
        while (pos < nums.size() && nums[pos] >= 0) pos += 2;

        // Step 2: Find the first misplaced negative
        while (neg < nums.size() && nums[neg] < 0) neg += 2;

        // Step 3: Swap if both pointers found misplaced elements
        if (pos < nums.size() && neg < nums.size()) {
            swap(nums[pos], nums[neg]);
        } else {
            // If either pointer goes out of bounds, break the loop
            break;
        }
    }
}

//// O(1) space uneven +,- order  maintained
void rearrangeMaintainOrder(vector<int>& nums) {
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            // Expect positive at even index
            if (nums[i] < 0) {
                // Find next positive element
                int j = i + 1;
                while (j < n && nums[j] < 0) j++;
                if (j == n) break; // No more positive numbers left
                // Rotate to bring the positive number to index i
                rotate(nums.begin() + i, nums.begin() + j, nums.begin() + j + 1);
            }
        } else {
            // Expect negative at odd index
            if (nums[i] >= 0) {
                // Find next negative element
                int j = i + 1;
                while (j < n && nums[j] >= 0) j++;
                if (j == n) break; // No more negative numbers left
                // Rotate to bring the negative number to index i
                rotate(nums.begin() + i, nums.begin() + j, nums.begin() + j + 1);
            }
        }
    }
}