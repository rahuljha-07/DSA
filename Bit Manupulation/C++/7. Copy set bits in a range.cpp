#include <iostream>
using namespace std;

/**
 * Function to copy set bits from `a` to `b` in the given range [left, right].
 * 
 * Explanation:
 * 1. Create a mask to isolate the bits in the range [left, right] in `a`.
 *    - Calculate the number of bits to copy: (right - left + 1).
 *    - Create a mask with these many bits set to 1 (e.g., 000...111).
 *    - Shift the mask to the left to align with the [left, right] range.
 *    - Perform bitwise AND with `a` to extract the bits in the range.
 * 2. Copy the bits to `b` using the OR operation (b | mask).
 * 
 * Time Complexity: O(1) (Bitwise operations are constant-time).
 * Space Complexity: O(1).
 */
int copySetBitsInRange(int a, int b, int left, int right) {
    // Step 1: Create a mask for the range [left, right]
    int mask = (1 << (right - left + 1)) - 1; // Create a mask with '1' in the range width
    mask = mask << (left - 1);                // Shift mask to align with the range
    mask = mask & a;                          // Extract the bits from `a` in the range

    // Step 2: Copy the extracted bits to `b`
    b = b | mask;

    return b; // Return the updated `b`
}

int main() {
    int a, b, left, right;

    // Input values
    cout << "Enter values for a, b, left, and right: " << endl;
    cin >> a >> b >> left >> right;

    // Copy the set bits from a to b in the given range
    int result = copySetBitsInRange(a, b, left, right);

    // Output the result
    cout << "Updated value of b: " << result << endl;

    return 0;
}
