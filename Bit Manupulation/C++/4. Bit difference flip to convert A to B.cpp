#include <iostream>
using namespace std;

// Function to count the number of bits to flip
int countBitsFlip(int A, int B) {
    int xorResult = A ^ B; // XOR A and B
    int count = 0;         // Initialize the count of bits to flip

    // Count the number of set bits in xorResult
    while (xorResult > 0) {
        count += xorResult & 1; // Check if the least significant bit is set
        xorResult = xorResult >> 1; // Right shift the result by 1
    }

    return count; // Return the total count
}

int main() {
    int A = 10, B = 20; // Example inputs
    cout << "Number of bits to flip to convert " << A << " to " << B << ": " 
         << countBitsFlip(A, B) << endl;

    return 0;
}
