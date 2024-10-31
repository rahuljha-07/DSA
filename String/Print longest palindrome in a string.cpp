#include <iostream>
#include <string>
using namespace std;

// Function to print the substring from the string based on given indices
void printSubStr(const string& str, int low, int high) {
    for (int i = low; i <= high; ++i) 
        cout << str[i]; 
}

// Function to find the longest palindromic substring
void longestPalindrome(string s) {
    int left, right;          // Indices for the left and right pointers
    int start = 0;           // Starting index of the longest palindrome found
    int maxLength = 1;       // Maximum length of the palindrome found

    // Loop through each character in the string
    for (int i = 1; i < s.length(); i++) {
        // Check for even-length palindromes
        left = i - 1;         // Set left pointer for even-length check
        right = i;            // Set right pointer for even-length check

        // Expand around the center
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            if (right - left + 1 > maxLength) { // Check if this palindrome is longer
                start = left;      // Update the starting index
                maxLength = right - left + 1; // Update the maximum length
            }
            left--;               // Move left pointer outwards
            right++;              // Move right pointer outwards
        }

        // Check for odd-length palindromes
        left = i - 1;          // Reset left pointer for odd-length check
        right = i + 1;         // Set right pointer for odd-length check

        // Expand around the center
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            if (right - left + 1 > maxLength) { // Check if this palindrome is longer
                start = left;      // Update the starting index
                maxLength = right - left + 1; // Update the maximum length
            }
            left--;               // Move left pointer outwards
            right++;              // Move right pointer outwards
        }
    }    

    // Print the longest palindromic substring
    printSubStr(s, start, start + maxLength - 1);
}

int main() {
    string s = "babad"; // Example input
    cout << "The longest palindromic substring is: ";
    longestPalindrome(s); // Call the function
    return 0;
}
