/**
 * This function calculates the number of set bits (1s) in the binary representation
 * of all integers from 0 to `num` and returns the results in a vector.
 * 
 * Key Insight:
 * There is a pattern in the sequence of set bits:
 * - For an even number `x`, the number of set bits is the same as `x / 2` (since shifting the binary representation
 *   to the right by 1 does not change the count of 1s).
 * - For an odd number `x`, the number of set bits is 1 more than `x / 2` (because the least significant bit is 1).
 * 
 * Example:
 * Binary representations and number of 1s:
 * 0 -> 0000 (0 ones)
 * 1 -> 0001 (1 one)
 * 2 -> 0010 (1 one)
 * 3 -> 0011 (2 ones)
 * 4 -> 0100 (1 one)
 * 5 -> 0101 (2 ones)
 * 6 -> 0110 (2 ones)
 * 7 -> 0111 (3 ones)
 * 8 -> 1000 (1 one)
 * 9 -> 1001 (2 ones)
 * 10 -> 1010 (2 ones)
 * 11 -> 1011 (3 ones)
 * 12 -> 1100 (2 ones)
 * 13 -> 1101 (3 ones)
 * 14 -> 1110 (3 ones)
 * 15 -> 1111 (4 ones)
 * 
 * To calculate for a number `x`:
 * - If `x` is even, the result is `countBits(x / 2)`.
 * - If `x` is odd, the result is `1 + countBits(x / 2)`.
 */

#include <iostream>
#include <vector>
using namespace std;

// Function to count the number of set bits in numbers from 0 to num
vector<int> countBits(int num) {
    vector<int> ans(num + 1); // Vector to store results for numbers 0 to num
    for (int i = 0; i <= num; i++) {
        ans[i] = rec(i); // Calculate the number of set bits for each number
    }
    return ans; // Return the vector
}

// Recursive function to count the number of set bits for a single number
int rec(int num) {
    if (num == 0) return 0; // Base case: 0 has 0 set bits
    if (num == 1) return 1; // Base case: 1 has 1 set bit
    if (num % 2 == 0) return rec(num / 2); // If even, use the result of num / 2
    else return 1 + rec(num / 2); // If odd, use 1 + result of num / 2
}

// Main function to demonstrate the solution
int main() {
    int num = 5; // Example input
    vector<int> result = countBits(num); // Call the function

    cout << "Number of set bits from 0 to " << num << ":\n";
    for (int i = 0; i <= num; i++) {
        cout << "Number: " << i << ", Set Bits: " << result[i] << endl;
    }

    return 0;
}
