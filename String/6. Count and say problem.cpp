#include <iostream>
#include <string>
using namespace std;

// Function to generate the nth element of the count-and-say sequence
string countAndSay(int n) {
    // Base case: if n is 1, return "1"
    if (n == 1) return "1";

    // Start the sequence with the second element for n = 2
    string s = "1"; // Initialize s as "1" for countAndSay(2)

    // Loop to generate the sequence from the 2nd element to the nth element
    for (int i = 2; i <= n; i++) {
        string t = ""; // Temporary string to hold the next term
        int c = 1;     // Counter to count occurrences of the current character

        // Iterate through the current string s
        for (int j = 1; j < s.length(); j++) {
            // If the current character is the same as the previous one
            if (s[j] == s[j - 1]) {
                c++; // Increment the counter
            } else {
                // If the current character is different, append the count and the character to t
                t += to_string(c) + s[j - 1];
                c = 1; // Reset the counter for the new character
            }
        }
        // Handle the last character (which wouldn't be added in the loop above)
        t += to_string(c) + s[s.length() - 1]; // Add the count and last character

        s = t; // Update s to the newly formed string for the next iteration
    }
    return s; // Return the final result
}

int main() {
    int n = 4; // Example input
    cout << "The " << n << "th element of the count-and-say sequence is: " << countAndSay(n) << endl;
    return 0;
}


