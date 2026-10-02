#include <iostream>
using namespace std;

/**
 * Approach 1: Using n & (n - 1)
 * 
 * This method checks if a number is a power of 2 by leveraging a key property:
 * - A number is a power of 2 if it has exactly one set bit in its binary representation.
 * - For a power of 2 (e.g., 8 -> 1000):
 *   - (n - 1) flips all bits after the rightmost set bit and the rightmost set bit itself.
 *   - Performing n & (n - 1) results in 0 because the rightmost set bit is cleared.
 * 
 * Time Complexity: O(1) (Single bitwise operation)
 * Space Complexity: O(1)
 */
bool isPowerOfTwoUsingBitwise(int n) {
    if (n <= 0) return false; // Negative numbers and 0 are not powers of 2
    return (n & (n - 1)) == 0; // Check if n has only one set bit
}

/**
 * Approach 2: Counting Set Bits
 * 
 * This method determines if a number is a power of 2 by counting the number of set bits (1s) in its binary representation.
 * - A number is a power of 2 if and only if it has exactly one set bit.
 * - This is done by checking each bit of the number using n & 1, and then right-shifting the number.
 * 
 * Steps:
 * 1. Count the number of set bits in n.
 * 2. If the count is 1, n is a power of 2.
 * 
 * Time Complexity: O(log(n)) (Proportional to the number of bits in n)
 * Space Complexity: O(1)
 */
bool isPowerOfTwoUsingCount(int n) {
    if (n <= 0) return false; // Negative numbers and 0 are not powers of 2
    int count = 0;
    while (n > 0) {
        count += (n & 1); // Check if the least significant bit is set
        n = n >> 1;       // Right shift to process the next bit
    }
    return count == 1; // A number is a power of 2 if it has exactly 1 set bit
}

int main() {
    int n = 8; // Example input

    // Approach 1: Using n & (n - 1)
    cout << "Using n & (n - 1): " << endl;
    cout << "Is " << n << " a power of 2? " << (isPowerOfTwoUsingBitwise(n) ? "true" : "false") << endl;

    // Approach 2: Counting Set Bits
    cout << "Using Counting Set Bits: " << endl;
    cout << "Is " << n << " a power of 2? " << (isPowerOfTwoUsingCount(n) ? "true" : "false") << endl;

    return 0;
}
