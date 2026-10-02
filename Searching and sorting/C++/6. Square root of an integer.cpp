#include <iostream>
using namespace std;

// Function to count the number of perfect squares less than a given number 'n'
int countSquares(int n) {
    int count = 0;  // Initialize count of squares to 0

    // Loop through numbers starting from 1
    for (int i = 1; i < n; i = i * i) {
        count++;  // Increment count for each perfect square found
    }
    
    return count;  // Return the final count of perfect squares
}

int main() {
    int n = 10;
    cout << "Number of perfect squares less than " << n << " is: " << countSquares(n) << endl;
    return 0;
}
