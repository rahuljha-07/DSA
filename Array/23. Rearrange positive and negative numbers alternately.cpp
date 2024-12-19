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
// Function to rearrange positive and negative
// integers in alternate fashion. The below
// solution doesn't maintain original order of
// elements
void rearrange(int arr[], int n)
{
    int i = 0, j = n-1;
 
    // shift all negative values to the end
    while (i < j) {
        while (i <= n - 1 and arr[i] > 0)
            i += 1;
        while (j >= 0 and arr[j] < 0)
            j -= 1;
        if (i < j )
            swap(arr[i], arr[j]);
    }
 
    // i has index of leftmost
    // negative element
    if (i == 0 || i == n)
        return;
 
    // start with first positive
    // element at index 0
 
    // Rearrange array in alternating
    // positive &
    // negative items
    int k = 0;
    while (k < n && i < n ) {
        // swap next positive
        // element at even position
        // from next negative element.
        swap(arr[k], arr[i]);
        i = i + 1;
        k = k + 2;
    }
}