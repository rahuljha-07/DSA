#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Function to solve and store all substrings in a vector
void solve(string input, string output, vector<string>& ans) {
    // Base case: If the input string is empty, store the output substring
    if (input.length() == 0) {
        if (output.length() > 0) ans.push_back(output); // Store the current substring in the vector
        return;
    } 

    // Exclude the first character from the output
    string excludeFirstChar = output; // Keep the output unchanged
    // Include the first character in the output
    string includeFirstChar = output; 
    includeFirstChar.push_back(input[0]); // Append the first character

    // Remove the first character from the input string
    input.erase(input.begin() + 0);

    // Recur with the remaining input string for both cases
    solve(input, excludeFirstChar, ans); // Call without including the character
    solve(input, includeFirstChar, ans); // Call with including the character
}

int main() {
    string s = "abc"; // Example input string
    vector<string> ans; // Vector to store all substrings
    solve(s, "", ans); // Start with an empty output string

    // Output all stored substrings
    cout << "All Substrings of '" << s << "':" << endl;
    for (const string& substring : ans) {
        cout << substring << endl; // Print each substring
    }
    
    return 0;
}
