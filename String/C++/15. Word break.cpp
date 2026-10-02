#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

// Function to perform word break and print all possible sentences
void wordBreak(string str, string ans, unordered_map<string, bool>& mp) {
    // If the entire string has been processed, print the sentence
    if (str.empty()) {
        cout << ans << endl;
        return;
    }

    // Traverse the string to break it into two parts
    for (int i = 1; i <= str.size(); ++i) {
        // Extract the left substring (prefix of the current length)
        string left = str.substr(0, i);

        // Check if the left part exists in the dictionary
        if (mp.find(left) != mp.end()) {
            // Call the function recursively with the remaining part (right substring)
            wordBreak(str.substr(i), ans + left + " ", mp);
        }
    }
}

int main() {
    // Example dictionary of words
    unordered_map<string, bool> dictionary = {
        {"apple", true}, {"pie", true}, {"pen", true}, {"applepen", true},
        {"pine", true}, {"pineapple", true}
    };

    // Input string to segment
    string input = "pineapplepenapple";
    
    // Call the function
    wordBreak(input, "", dictionary);

    return 0;
}
