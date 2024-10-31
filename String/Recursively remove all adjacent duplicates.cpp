#include <iostream>
#include <string>

using namespace std;

// Function to remove adjacent duplicates recursively
string removeAdjacentDuplicates(const string& S) {
    // Base case: if the string is empty or has one character, return it
    if (S.empty() || S.length() == 1) {
        return S;
    }

    string result;  // To store the result after removing duplicates
    bool hasAdjacentDuplicates = false;  // Flag to check if duplicates were found

    // Iterate through the string to find adjacent duplicates
    for (int i = 0; i < S.length(); i++) {
        // Check if the current character is the same as the next one
        if (i < S.length() - 1 && S[i] == S[i + 1]) {
            hasAdjacentDuplicates = true;  // Set the flag to true
            // Skip all adjacent duplicates
            while (i < S.length() - 1 && S[i] == S[i + 1]) {
                i++;  // Move the index forward to skip duplicates
            }
        } else {
            result += S[i];  // Add non-duplicate characters to result
        }
    }

    // If adjacent duplicates were found, call the function recursively
    return hasAdjacentDuplicates ? removeAdjacentDuplicates(result) : result;
}

int main() {
    string input1 = "geeksforgeek";
    string input2 = "abccbccba";

    cout << "Input: " << input1 << " -> Output: " << removeAdjacentDuplicates(input1) << endl;
    cout << "Input: " << input2 << " -> Output: " << removeAdjacentDuplicates(input2) << endl;

    return 0;
}
