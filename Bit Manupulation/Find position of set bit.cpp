#include <iostream>
using namespace std;

/**
 * Function to find the position of the only set bit in N.
 * 
 * Explanation:
 * 1. A number has exactly one set bit if it is a power of 2.
 *    - Use the property (N & (N - 1)) == 0 to check if N is a power of 2.
 *    - If N is not a power of 2 (no set bits or multiple set bits), return -1.
 * 2. If N is a power of 2, the task is to find the position of the only set bit.
 *    - Right shift the number (N >> 1) until the least significant bit (LSB) is 1.
 *    - Count how many shifts were performed. The position is the count + 1 (starting from 1).
 * 
 * Example 1:
 * Input: N = 2
 * Binary: 10
 * N & (N - 1) = 10 & 01 = 00 → Valid (power of 2)
 * Position: Start at LSB (position 1), after 1 shift, LSB is 1 → Position = 2
 * Output: 2
 * 
 * Example 2:
 * Input: N = 5
 * Binary: 101
 * N & (N - 1) = 101 & 100 = 100 ≠ 0 → Invalid (not a power of 2)
 * Output: -1
 * 
 * Time Complexity: O(log N) → Depends on the number of bits in N.
 * Space Complexity: O(1) → Only a few variables are used.
 */
int findPositionOfSetBit(int N) {
    /**
     * Step 1: Check if N is a power of 2.
     * A power of 2 has only one set bit.
     * Use the condition (N & (N - 1)) == 0 to validate.
     */
    if (N <= 0 || (N & (N - 1)) != 0) {
        return -1; // Return -1 if N is not a power of 2
    }

    /**
     * Step 2: Find the position of the set bit.
     * Initialize position to 1 (counting starts from 1).
     * Right shift N until the least significant bit (LSB) is 1.
     */
    int position = 1;
    while ((N & 1) == 0) { // Check if LSB is 0
        N = N >> 1; // Right shift N by 1
        position++; // Increment position counter
    }

    return position; // Return the position of the set bit
}

int main() {
    int N;

    // Example 1: Input N = 2
    N = 2;
    cout << "Position of set bit in " << N << ": " << findPositionOfSetBit(N) << endl;

    // Example 2: Input N = 5
    N = 5;
    cout << "Position of set bit in " << N << ": " << findPositionOfSetBit(N) << endl;

    // Example 3: Input N = 16
    N = 16;
    cout << "Position of set bit in " << N << ": " << findPositionOfSetBit(N) << endl;

    return 0;
}
