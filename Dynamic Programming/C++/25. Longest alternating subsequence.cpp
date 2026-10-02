#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> a = {1, 5, 4, 9, 2};
    cout << "Length of Longest Alternating Subsequence: " << AlternatingMaxLength(a) << endl;
    return 0;
}

//another O(n)
int AlternatingMaxLength(vector<int>& a) {
    int n = a.size();
    if (n == 1) return 1;

    int inc = 1; // Length of increasing subsequence
    int dec = 1; // Length of decreasing subsequence

    for (int i = 1; i < n; i++) {
        if (a[i] > a[i - 1]) {
            // Current element is greater, so extend the decreasing sequence
            inc = dec + 1;
        } else if (a[i] < a[i - 1]) {
            // Current element is smaller, so extend the increasing sequence
            dec = inc + 1;
        }
    }

    // The result is the maximum length of either an increasing or decreasing sequence
    return max(inc, dec);
}

/*
    Intuition Behind the Approach:
    ---------------------------------
    The problem requires us to find the longest alternating subsequence, meaning the elements should alternate between 
    increasing and decreasing trends. Instead of storing the entire subsequence, we can efficiently track the longest 
    alternating subsequence using two variables.

    Step 1: Understanding the Pattern
    ---------------------------------
    A valid alternating subsequence follows either of the two patterns:
    - Increasing: x1 < x2 > x3 < x4 > x5 ...
    - Decreasing: x1 > x2 < x3 > x4 < x5 ...

    Key Insight:
    - If arr[i] > arr[i-1], it means we are currently in an increasing pattern.
    - If arr[i] < arr[i-1], it means we are currently in a decreasing pattern.
    - Using this, we can track the longest alternating subsequence dynamically.

    Step 2: Defining States
    ---------------------------------
    We maintain two variables:
    1. `up`   -> Length of the longest alternating subsequence ending with an increasing trend.
    2. `down` -> Length of the longest alternating subsequence ending with a decreasing trend.

    Step 3: Observing the Transition
    ---------------------------------
    We iterate through the array and update `up` and `down` based on the current element:
    - Case 1: arr[i] > arr[i-1]  (Increasing trend)
        -> We must have had a decreasing sequence before it.
        -> Update `up = down + 1` (Extend the previous decreasing sequence)
    - Case 2: arr[i] < arr[i-1]  (Decreasing trend)
        -> We must have had an increasing sequence before it.
        -> Update `down = up + 1` (Extend the previous increasing sequence)
    - Case 3: arr[i] == arr[i-1]  (No change)
        -> The sequence remains the same, so we ignore this element.

    Final Answer:
    ---------------------------------
    The result is max(up, down), which gives the longest alternating subsequence.

    Step 4: Dry Run Example
    ---------------------------------
    Input: arr = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    Expected Output: 7

    Iterations:
    Index | arr[i] | up  | down | Explanation
    ---------------------------------
      0   |   1    |  1  |  1   | Start with a single element
      1   |  17    |  2  |  1   | 1 < 17, so `up = down + 1 = 2`
      2   |   5    |  2  |  3   | 17 > 5, so `down = up + 1 = 3`
      3   |  10    |  4  |  3   | 5 < 10, so `up = down + 1 = 4`
      4   |  13    |  4  |  3   | 10 < 13, no decrease before, `up` remains 4
      5   |  15    |  4  |  3   | 13 < 15, still increasing, no effect
      6   |  10    |  4  |  5   | 15 > 10, so `down = up + 1 = 5`
      7   |   5    |  4  |  5   | 10 > 5, still decreasing, no effect
      8   |  16    |  6  |  5   | 5 < 16, so `up = down + 1 = 6`
      9   |   8    |  6  |  7   | 16 > 8, so `down = up + 1 = 7`

    Final answer: max(up, down) = max(6, 7) = 7

    Step 5: Complexity Analysis
    ---------------------------------
    - Time Complexity: O(n)   -> We only loop through the array once.
    - Space Complexity: O(1)  -> We only use two extra variables (`up` and `down`).

    Why This Works?
    ---------------------------------
    - Instead of storing an entire subsequence, we only track two key values (`up` and `down`).
    - This greedy approach ensures we always keep the longest alternating subsequence without explicitly storing it.

    Alternative Approach: Dynamic Programming (O(n) Space)
    ---------------------------------
    - We can also use Dynamic Programming (DP) where dp[i] stores the longest alternating subsequence up to index `i`.
    - However, this would require O(n) extra space, which is unnecessary given our optimized solution.

    Final Thoughts:
    ---------------------------------
    This greedy approach allows us to solve the problem in O(n) time with O(1) space, making it optimal.
*/
