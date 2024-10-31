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
void permute(string ip, string op, vector<string>& v) {
    // Base case: If input string is empty, add the current permutation to the result
    if (ip.size() == 0) {
        v.push_back(op); // Store the generated permutation
        return;
    }

    // Using an unordered set to keep track of characters already included at this level
    unordered_set<char> mp; // Set to store characters that have been used in this recursive call
    for (int i = 0; i < ip.size(); i++) {
        // Check if the character is already used in this position
        if (mp.find(ip[i]) == mp.end()) {
            mp.insert(ip[i]); // Mark the character as used
            // Create a new input string by removing the current character
            string newip = ip.substr(0, i) + ip.substr(i + 1);
            // Create a new output string by adding the current character
            string newop = op + ip[i];
            // Recur with the new input and output strings
            permute(newip, newop, v);
        }
    }
}

// Function to find all unique permutations of a given string
vector<string> find_permutation(string S) {
    // Initialize a vector to store the permutations
    vector<string> v; 
    // Call the permute function to generate permutations
    permute(S, "", v);
    return v; // Return the vector containing all unique permutations
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
