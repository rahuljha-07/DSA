#include <iostream>
using namespace std;

// Function to count the number of set bits in an integer `n`
int countSetBits(int n) {
    int result = 0;  // Variable to store the count of set bits
    int helper = 1;  // Helper variable initialized to 1 (binary: 0001)

    // Loop through all 32 bits (for 32-bit integers)
    for (int i = 1; i <= 32; i++) {
        // Check if the bit at the current position is set
        if ((helper & n) != 0) { // Perform bitwise AND between `helper` and `n`
            result++; // Increment the result if the bit is set
        }

        // Left shift `helper` by 1 to check the next bit in the next iteration
        helper = helper << 1;
    }

    // Return the total count of set bits
    return result;
}

int main() {
    int n = 11; // Example input
    cout << "Number of set bits in " << n << " is: " << countSetBits(n) << endl;
    return 0;
}

/*
Example: Counting set bits for n = 11
Binary representation of n: 1011

Iteration steps:
1. helper = 0001, (helper & n) = 0001 & 1011 = 0001 -> result = 1
   Shift helper: helper = 0010
2. helper = 0010, (helper & n) = 0010 & 1011 = 0010 -> result = 2
   Shift helper: helper = 0100
3. helper = 0100, (helper & n) = 0100 & 1011 = 0000 -> result = 2
   Shift helper: helper = 1000
4. helper = 1000, (helper & n) = 1000 & 1011 = 1000 -> result = 3
   Shift helper: helper = 10000
5. Remaining iterations: All higher bits of n are 0, result remains 3.

Final result: 3 set bits in the binary representation of 11.
*/
