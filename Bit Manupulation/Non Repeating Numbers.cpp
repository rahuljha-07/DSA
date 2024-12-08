#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/*
Explanation:

Given array: {36, 50, 24, 56, 36, 24, 42, 50}

Step 1: XOR all numbers in the array.
Binary representations:
36 -> 100100
50 -> 110010
24 -> 011000
56 -> 111000
36 -> 100100
24 -> 011000
42 -> 101010
50 -> 110010

XOR Result (xxory):
100100
^ 110010 = 010110
^ 011000 = 001110
^ 111000 = 110110
^ 100100 = 010010
^ 011000 = 001010
^ 101010 = 100000
^ 110010 = 010010
Final xxory = 010010 (binary) = 42 (decimal)

Step 2: Find the rightmost set bit (RMSB) in `xxory`.
- RMSB = xxory & -xxory
  010010 (binary of 42)
& 101110 (binary of -42 in two's complement)
= 000010 (decimal = 2)

Step 3: Split numbers into two groups based on the RMSB.
- Group 1: Numbers with the bit set at position RMSB.
- Group 2: Numbers with the bit unset at position RMSB.

Group 1: {50, 24, 56, 24}
Group 2: {36, 36, 42, 50}

Step 4: XOR numbers in each group to isolate the two non-repeating numbers.
Group 1 XOR: 50 ^ 24 ^ 56 ^ 24 = 56
Group 2 XOR: 36 ^ 36 ^ 42 ^ 50 = 42

Result: Non-repeating numbers are {42, 56}.
*/

vector<int> findNonRepeatingNumbers(vector<int>& arr) {
    int xxory = 0;

    // Step 1: XOR all numbers in the array
    for (int val : arr) {
        xxory ^= val;
    }

    // Step 2: Find the rightmost set bit (RMSB)
    int rsbm = xxory & -xxory;

    int x = 0, y = 0;

    // Step 3: Split numbers into two groups and XOR within each group
    for (int val : arr) {
        if ((val & rsbm) == 0) {
            x ^= val; // Group 1: Numbers where RMSB is 0
        } else {
            y ^= val; // Group 2: Numbers where RMSB is 1
        }
    }

    // Step 4: Sort the results to ensure the output is in increasing order
    vector<int> result = {x, y};
    sort(result.begin(), result.end());
    return result;
}

int main() {
    vector<int> arr = {36, 50, 24, 56, 36, 24, 42, 50}; // Input array
    vector<int> result = findNonRepeatingNumbers(arr); // Find the two non-repeating numbers

    // Print the result
    cout << "The two non-repeating numbers are: " << result[0] << " and " << result[1] << endl;

    return 0;
}
