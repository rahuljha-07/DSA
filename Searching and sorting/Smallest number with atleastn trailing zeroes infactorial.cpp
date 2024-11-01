#include <iostream>
using namespace std;

// Function to check if the factorial of a number `p` has at least `n` trailing zeroes
bool hasAtLeastNTrailingZeroes(int number, int requiredZeroes) {
    int temp = number;  // Store the original number for calculations
    int count = 0;      // Counter for trailing zeroes
    int factor = 5;     // Initial factor for trailing zeroes calculation

    // Count the number of trailing zeroes contributed by factors of 5
    while (factor <= temp) {
        count += temp / factor; // Count how many multiples of `factor` are in `temp`
        factor *= 5;            // Move to the next power of 5
    }

    // Return true if the count of trailing zeroes is at least `requiredZeroes`
    return (count >= requiredZeroes);
}

// Function to find the smallest number whose factorial contains at least `n` trailing zeroes
int findSmallestFactorialNumberWithTrailingZeroes(int n) {
    // Special case: If n is 1, the smallest number is 5 (since 5! has 1 trailing zero)
    if (n == 1) return 5;

    int low = 0;             // Lower bound for binary search
    int high = 5 * n;       // Upper bound for binary search
    int result = -1;        // Variable to store the result

    // Binary search to find the smallest number with at least `n` trailing zeroes
    while (low < high) {
        int mid = (low + high) / 2;  // Calculate the middle point
        if (hasAtLeastNTrailingZeroes(mid, n)) {
            high = mid;  // If mid has at least n trailing zeroes, search in the left half
        } else {
            low = mid + 1; // Otherwise, search in the right half
        }
    }

    return low; // Return the smallest number found
}

int main() {
    int n;

    // Example usage
    cout << "Enter the number of trailing zeroes: ";
    cin >> n;
    int result = findSmallestFactorialNumberWithTrailingZeroes(n);
    cout << "The smallest number whose factorial has at least " << n << " trailing zeroes is: " << result << endl;

    return 0;
}
