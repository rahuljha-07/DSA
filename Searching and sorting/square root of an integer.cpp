#include <iostream>
using namespace std;

// Function to count the number of perfect squares less than a given number 'n'
int countSquares(int n) {
    int count = 0;  // Initialize count of squares to 0

    // Loop through numbers starting from 1, check if their square is less than 'n'
    for (int i = 1; i * i < n; i++) {
        count++;  // Increment count if i*i is less than n
    }
    
    return count;  // Return the final count of perfect squares
}

int main() {
    int n = 10;
    cout << "Number of perfect squares less than " << n << " is: " << countSquares(n) << endl;
    return 0;
}
