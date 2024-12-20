#include <iostream>
#include <string>
using namespace std;
// To solve the problem of splitting a binary string into the maximum number of consecutive substrings with an equal number of 0s and 1s, we can follow these steps:

// Initialize Counters: We'll maintain a count of 0s and 1s as we iterate through the string.
// Count Balanced Substrings: Every time the counts of 0s and 1s are equal, we can conclude that we have found a balanced substring. We'll increment a counter to keep track of the number of such substrings.
// Check for Imbalance: If we reach the end of the string and have not seen a balanced count, we can conclude that splitting is impossible.

int maxBalancedSubstrings(const string& str) {
    int count0 = 0, count1 = 0;
    int maxCount = 0;

    // Iterate through the binary string
    for (char ch : str) {
        if (ch == '0') {
            count0++; // Increment count of 0s
        } else {
            count1++; // Increment count of 1s
        }

        // If the counts of 0s and 1s are equal, we found a balanced substring
        if (count0 == count1) {
            maxCount++; // Increment the balanced substring count
        }
    }

    // Check if the total counts of 0s and 1s are equal
    if (count0 != count1) {
        return -1; // Not possible to split the string into balanced substrings
    }

    return maxCount; // Return the maximum count of balanced substrings
}

int main() {
    // Example inputs
    string str1 = "0100110101";
    string str2 = "0111100010";
    string str3 = "0000000000";

    cout << "Input: " << str1 << " -> Output: " << maxBalancedSubstrings(str1) << endl;
    cout << "Input: " << str2 << " -> Output: " << maxBalancedSubstrings(str2) << endl;
    cout << "Input: " << str3 << " -> Output: " << maxBalancedSubstrings(str3) << endl;

    return 0;
}
