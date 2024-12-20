#include <iostream>
#include <string>
using namespace std;

// Function to find the longest palindromic substring
string longestPalindrome(string s) {
    if (s.empty()) return ""; // Handle edge case: empty string
    
    int left, right;          // Indices for the left and right pointers
    int start = 0;            // Starting index of the longest palindrome found
    int maxLength = 1;        // Maximum length of the palindrome found

    // Loop through each character in the string
    for (int i = 1; i < s.length(); i++) {
        // Check for even-length palindromes
        left = i - 1;
        right = i;

        // Expand around the center
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            if (right - left + 1 > maxLength) { // Check if this palindrome is longer
                start = left;
                maxLength = right - left + 1;
            }
            left--;
            right++;
        }

        // Check for odd-length palindromes
        left = i - 1;
        right = i + 1;

        // Expand around the center
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            if (right - left + 1 > maxLength) { // Check if this palindrome is longer
                start = left;
                maxLength = right - left + 1;
            }
            left--;
            right++;
        }
    }

    // Return the longest palindromic substring
    return s.substr(start, maxLength);
}

int main() {
    string s = "babad"; // Example input
    cout << "The longest palindromic substring is: " << longestPalindrome(s) << endl;
    return 0;
}
