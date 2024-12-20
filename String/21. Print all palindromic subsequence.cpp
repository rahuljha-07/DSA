#include <bits/stdc++.h>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

// Memoization map
unordered_map<string, vector<string>> memo;

vector<string> countPalindromicSubsequences(const string& str, int start, int end) {
    // Create a unique key for the current substring
    string key = to_string(start) + "_" + to_string(end);
    
    // Check if the result is already memoized
    if (memo.find(key) != memo.end()) {
        return memo[key];
    }

    vector<string> result;

    // Base case: if the substring is empty
    if (start > end) {
        return result; // no palindromic subsequences
    }
    
    // Base case: if the substring has one character
    if (start == end) {
        result.push_back(string(1, str[start])); // single character is a palindrome
        return result;
    }

    // If characters at the start and end are the same
    if (str[start] == str[end]) {
        // Include both characters
        vector<string> innerSubseqs = countPalindromicSubsequences(str, start + 1, end - 1);
        for (const string& subseq : innerSubseqs) {
            result.push_back(str[start] + subseq + str[end]); // add the characters to both ends
        }
        
        // Add the single characters as palindromes
        result.push_back(string(1, str[start]));
        result.push_back(string(1, str[end]));
    }
    
    // Count palindromic subsequences excluding either the start or end character
    vector<string> leftSubseqs = countPalindromicSubsequences(str, start + 1, end);
    vector<string> rightSubseqs = countPalindromicSubsequences(str, start, end - 1);
    
    // Merge results while ensuring uniqueness
    result.insert(result.end(), leftSubseqs.begin(), leftSubseqs.end());
    result.insert(result.end(), rightSubseqs.begin(), rightSubseqs.end());

    // Remove duplicates by converting to a set then back to vector (optional)
    sort(result.begin(), result.end());
    result.erase(unique(result.begin(), result.end()), result.end());

    // Memoize the result
    memo[key] = result;
    return result;
}

int main() {
    string str = "abcadb"; // Example input
    vector<string> palindromicSubsequences = countPalindromicSubsequences(str, 0, str.length() - 1);
    
    cout << "Number of palindromic subsequences: " << palindromicSubsequences.size() << endl;
    cout << "Palindromic Subsequences: ";
    for (const string& subseq : palindromicSubsequences) {
        cout << subseq << " ";
    }
    cout << endl;

    return 0;
}
