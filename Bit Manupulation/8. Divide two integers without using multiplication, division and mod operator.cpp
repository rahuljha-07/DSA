#include <iostream>
#include <climits>
using namespace std;

/**
 * Function to divide two integers without using multiplication, division, or modulo.
 * 
 * Steps:
 * 1. Handle edge cases (e.g., division by 0, overflow).
 * 2. Determine the sign of the result.
 * 3. Use bit manipulation to calculate the quotient by:
 *    - Repeatedly subtracting or shifting the divisor.
 * 4. Clamp the result to the range [-2^31, 2^31 - 1].
 * 
 * Time Complexity: O(log(a))
 * Space Complexity: O(1)
 */
int divide(int a, int b) {
    // Edge case: Division by 0
    if (b == 0) return INT_MAX; // Division by 0 is undefined

    // Edge case: Overflow when a is INT_MIN and b is -1
    if (a == INT_MIN && b == -1) return INT_MAX;

    // Determine the sign of the result
    bool negative = (a < 0) ^ (b < 0); // XOR to check if signs are different

    // Use absolute values to simplify calculations
    long long dividend = abs((long long)a); // Convert to long long to handle overflow
    long long divisor = abs((long long)b);

    long long quotient = 0;

    // Perform bit manipulation to find the quotient
    while (dividend >= divisor) {
        long long temp = divisor, multiple = 1;

        // Double the divisor until it exceeds the dividend
        while ((temp << 1) <= dividend) {
            temp <<= 1;      // Double the divisor
            multiple <<= 1;  // Double the multiplier
        }

        dividend -= temp;    // Subtract the largest shifted divisor
        quotient += multiple; // Add the corresponding multiple to the quotient
    }

    // Apply the sign to the result
    if (negative) quotient = -quotient;

    // Clamp the result to the 32-bit integer range
    if (quotient > INT_MAX) return INT_MAX;
    if (quotient < INT_MIN) return INT_MIN;

    return quotient;
}

int main() {
    // Example inputs
    int a = 10, b = 3;
    cout << "Quotient of " << a << " / " << b << " = " << divide(a, b) << endl;

    a = 43, b = -8;
    cout << "Quotient of " << a << " / " << b << " = " << divide(a, b) << endl;

    a = INT_MIN, b = 1;
    cout << "Quotient of " << a << " / " << b << " = " << divide(a, b) << endl;

    return 0;
}
