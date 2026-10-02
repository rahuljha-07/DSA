#include <iostream>
#include <vector>
#include <algorithm> // For sort function
using namespace std;

// Function to generate all permutations of the string using recursion and backtracking
void permute(string s, int start, int end, vector<string>& ans) {
    // Base case: If the start index equals the end index, a permutation is complete
    if (start == end) {
        ans.push_back(s); // Store the current permutation in the vector
    } else {
        // Iterate through the characters of the string
        for (int i = start; i <= end; i++) {
            // Swap the current character with the start character
            swap(s[i], s[start]);
            // Recur to generate permutations of the remaining characters
            permute(s, start + 1, end, ans);
            // Backtrack: Swap back to the original configuration
            swap(s[i], s[start]);
        }
    }
}

// Function to find all permutations of a string
vector<string> find_permutation(string s) {
    vector<string> ans; // Vector to store all permutations
    int n = s.size(); // Get the length of the string
    if (n == 0) return ans; // Return an empty vector if the string is empty

    // Call the permute function to generate permutations
    permute(s, 0, n - 1, ans);
    // Sort the results to ensure permutations are in lexicographical order
    sort(ans.begin(), ans.end());
    return ans; // Return the vector containing all permutations
}

//using ip op method
// Function to generate permutations
void solve(string input, string output, vector<string>& ans) {
    // Base case: If the input string is empty, store the permutation
    if (input.length() == 0) {
        ans.push_back(output); // Store the current permutation in the vector
        return;
    }

    // Generate permutations by choosing each character as the next one
    for (int i = 0; i < input.length(); i++) {
        // Form a new input string excluding the current character
        string remaining = input.substr(0, i) + input.substr(i + 1);
        // Include the current character in the output
        solve(remaining, output + input[i], ans);
    }
}

// Function to find all unique permutations of a given string
vector<string> find_permutation(string S) {
    // Initialize a vector to store the permutations
    vector<string> ans; 
    // Call the permute function to generate permutations
     solve(s, "", ans);
    return ans; // Return the vector containing all unique permutations
}

// Example usage
int main() {
    string s = "abc"; // Example input string
    vector<string> permutations = find_permutation(s); // Find permutations

    // Print all permutations
    cout << "Permutations of '" << s << "':" << endl;
    for (const string& permutation : permutations) {
        cout << permutation << endl; // Print each permutation
    }
    
    return 0;
}
