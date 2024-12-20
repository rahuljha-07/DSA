#include <string>
#include <algorithm> // For the min function
using namespace std;

/*
 * Function to calculate the minimum number of flips required to 
 * convert a binary string into an alternating character sequence.
 * Parameters:
 * - s: A binary string containing only '0's and '1's.
 *
 * Returns:
 * - The minimum number of bits that need to be flipped.
 */
int minFlipsToAlternating(string s) {
    int countFlipsToPattern1 = 0; // Flips needed for the pattern "010101..."
    int countFlipsToPattern2 = 0; // Flips needed for the pattern "101010..."

    // Iterate through the string to count flips needed for both patterns
    for (int i = 0; i < s.length(); i++) {
        // Check against the first pattern
        if (i % 2 == 0) { // Even index
            if (s[i] == '1') countFlipsToPattern1++; // Expecting '0'
        } else { // Odd index
            if (s[i] == '0') countFlipsToPattern1++; // Expecting '1'
        }

        // Check against the second pattern
        if (i % 2 == 0) { // Even index
            if (s[i] == '0') countFlipsToPattern2++; // Expecting '1'
        } else { // Odd index
            if (s[i] == '1') countFlipsToPattern2++; // Expecting '0'
        }
    }

    // Return the minimum flips required to convert to either pattern
    return min(countFlipsToPattern1, countFlipsToPattern2);
}

// Example usage
int main() {
    string binaryString = "001";
    int result = minFlipsToAlternating(binaryString);
    cout << "Minimum number of flips: " << result << endl; // Output: 1
    return 0;
}
