#include <iostream>
using namespace std;

/**
 * Function to calculate the square of a number without using *, /, or pow().
 * 
 * Explanation:
 * 1. Binary Representation of a Number:
 *    - Any number `x` can be represented in binary as a sum of powers of 2.
 *      For example:
 *        - 5 = 101 in binary = 2^2 + 2^0
 *        - To square `5`, you can decompose the problem:
 *          5^2 = (2^2 + 2^0)^2 = 5 * 5 = 25
 *    - Each bit of the binary representation of `x` contributes to the square.
 * 
 * 2. Algorithm:
 *    - Use bitwise shifts to calculate powers of 2.
 *    - For each bit in the binary representation of `x`:
 *      - If the bit is set (1), add the result of shifting `n` left by the bit position.
 *      - Shifting left by `i` (n << i) is equivalent to multiplying `n` by 2^i.
 *    - Sum all the contributions to get the final square.
 * 
 * Example:
 * Input: n = 5
 * Binary representation of 5 = 101
 * 5^2 = (5 << 2) + (5 << 0) = 20 + 5 = 25
 * 
 * Time Complexity: O(log n) (Proportional to the number of bits in the input).
 * Space Complexity: O(1).
 */
int square(int n) {
    int result = 0; // Initialize the result

    // Make the number positive (to handle negative inputs)
    int x = abs(n);

    int i = 0; // Bit position
    while (x > 0) {
        /**
         * Check if the ith bit of x is set.
         * If it is, add (n << i) to the result.
         * - n << i is equivalent to n multiplied by 2^i.
         */
        if (x & 1) {
            result += (n << i); // Add the shifted value to the result
        }

        // Move to the next bit by right-shifting x
        x = x >> 1;

        // Increment the bit position
        i++;
    }

    return result;
}

int main() {
    int n;

    // Input
    cout << "Enter a number: ";
    cin >> n;

    // Calculate square
    cout << "Square of " << n << " is: " << square(n) << endl;

    return 0;
}
