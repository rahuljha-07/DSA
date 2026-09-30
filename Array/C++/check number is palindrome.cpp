#include <iostream>
#include <vector>

using namespace std;

// Function to check if a number is a palindrome
bool isPalindrome(int num) {
    int original = num; // Store the original number
    int reversed = 0;   // Variable to store the reversed number

    // Reverse the number
    while (num > 0) {
        int digit = num % 10;            // Get the last digit
        reversed = reversed * 10 + digit; // Build the reversed number
        num /= 10;                       // Remove the last digit
    }

    // Check if the original number is equal to the reversed number
    return original == reversed;
}

int main() {
    vector<int> arr = {111, 121, 134}; // Example array

    // Check each number in the array and print whether it's a palindrome
    for (int num : arr) {
        if (isPalindrome(num)) {
            cout << num << " is a palindrome." << endl;
        } else {
            cout << num << " is not a palindrome." << endl;
        }
    }

    return 0;
}
