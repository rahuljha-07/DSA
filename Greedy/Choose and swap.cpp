#include <bits/stdc++.h>
using namespace std;

// Function to find the lexicographically smallest string
string chooseAndSwap(string str) {
    set<char> remainingChars; // Set to store remaining characters
    int n = str.length();

    // Step 1: Add all characters of the string to the set
    for (int i = 0; i < n; i++) {
        remainingChars.insert(str[i]);
    }

    // Step 2: Iterate through the string
    for (int i = 0; i < n; i++) {
        // Remove the current character from the set (as it's already visited)
        remainingChars.erase(str[i]);

        // If no remaining characters, break
        if (remainingChars.empty()) {
            break;
        }

        // Find the smallest character in the remaining set
        char smallestChar = *remainingChars.begin();

        // Check if swapping the current character with the smallest character is beneficial
        if (smallestChar < str[i]) {
            char currentChar = str[i];

            // Step 3: Perform the swap operation
            for (int j = 0; j < n; j++) {
                if (str[j] == currentChar) {
                    str[j] = smallestChar;
                } else if (str[j] == smallestChar) {
                    str[j] = currentChar;
                }
            }

            // Break after the first beneficial swap
            break;
        }
    }

    // Return the resulting string
    return str;
}

// Example usage
int main() {
    string str = "ccad";
    cout << "Original string: " << str << endl;
    string result = chooseAndSwap(str);
    cout << "Lexicographically smallest string: " << result << endl;

    str = "abba";
    cout << "Original string: " << str << endl;
    result = chooseAndSwap(str);
    cout << "Lexicographically smallest string: " << result << endl;

    return 0;
}
