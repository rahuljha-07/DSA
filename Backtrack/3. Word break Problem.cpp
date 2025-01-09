#include <iostream>
#include <unordered_set>
#include <string>
#include <vector>

using namespace std;

// Function to perform the word break using backtracking
void solve(const string& str, string currentSentence, const unordered_set<string>& dictionary, vector<string>& results) {
    // Base case: if the string size is zero, add the constructed sentence to the results and return
    if (str.size() == 0) {
        results.push_back(currentSentence);
        return;
    }

    // Iterate through the string to find all possible prefixes
    for (size_t i = 0; i < str.size(); ++i) {
        string prefix = str.substr(0, i + 1); // Extract the prefix
        if (dictionary.find(prefix) != dictionary.end()) { // Check if prefix is in the dictionary
            string remaining = str.substr(i + 1); // Get the remaining part of the string
            // Recur with the remaining string and add the prefix to the current sentence
            solve(remaining, currentSentence + prefix + (remaining.empty() ? "" : " "), dictionary, results);
        }
    }
}

// Wrapper function to initiate the word break
vector<string> wordBreak(const string& str, const unordered_set<string>& dictionary) {
    vector<string> results; // Vector to store all valid sentences
    solve(str, "", dictionary, results);
    return results;
}

int main() {
    // Example usage
    string inputString = "catsanddog";
    unordered_set<string> dictionary = {"cat", "cats", "and", "sand", "dog"};

    vector<string> results = wordBreak(inputString, dictionary);

    // Print all results
    cout << "All possible word breaks:\n";
    for (const string& sentence : results) {
        cout << sentence << endl;
    }

    return 0;
}
