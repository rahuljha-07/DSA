#include <iostream>
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

    for (int i = 0; i < s.length(); i++) {
        if (i % 2 == 0) { // Checking for even index
            if (s[i] == '1') { 
                countFlipsToPattern1++; // Pattern 1 needs to increment for '1' at even
            } else { 
                countFlipsToPattern2++; // Pattern 2 needs to increment for '0' at even
            }
        } else { // i % 2 != 0, checking for odd index
            if (s[i] == '0') { 
                countFlipsToPattern1++; // Pattern 1 needs to increment for '0' at odd
            } else { 
                countFlipsToPattern2++; // Pattern 2 needs to increment for '1' at odd
            }
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
