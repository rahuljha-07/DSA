#include <bits/stdc++.h>
using namespace std;

// Helper function to generate permutations
void generatePermutations(string &str, int startIndex, vector<string> &result) {
    // Base case: If startIndex is at the end of the string, store the permutation
    if (startIndex == str.size() - 1) {
        result.push_back(str);
        return;
    }

    // Iterate through the string and swap characters to generate permutations
    for (int i = startIndex; i < str.size(); i++) {
        // Swap the current character with the character at startIndex
        swap(str[startIndex], str[i]);

        // Recursively generate permutations for the remaining string
        generatePermutations(str, startIndex + 1, result);

        // Backtrack: Restore the original order of the string
        swap(str[startIndex], str[i]);
    }
}

// Function to print all permutations of a given string
void printPermutations(string str) {
    vector<string> result;

    // Generate all permutations
    generatePermutations(str, 0, result);

    // Sort the permutations to ensure they are printed in lexicographical order
    sort(result.begin(), result.end());

    // Print the permutations
    for (const string &perm : result) {
        cout << perm << endl;
    }
}

// Driver code
int main() {
    string inputString;

    cout << "Enter a string: ";
    cin >> inputString;

    cout << "Permutations of the string are:\n";
    printPermutations(inputString);

    return 0;
}
