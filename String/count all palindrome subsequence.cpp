#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;

// Memoization map
unordered_map<string, int> memo;

int countPalindromicSubsequences(const string& str, int start, int end) {
    // Create a unique key for the current substring
    string key = to_string(start) + "_" + to_string(end);
    
    // Check if the result is already memoized
    if (memo.find(key) != memo.end()) {
        return memo[key];
    }

    // Base case: if the substring is empty
    if (start > end) {
        return 0; // no palindromic subsequences
    }
    
    // Base case: if the substring has one character
    if (start == end) {
        return 1; // single character is a palindrome
    }

    int count = 0;

    // If characters at the start and end are the same
    if (str[start] == str[end]) {
        // Include both characters
        count += countPalindromicSubsequences(str, start + 1, end - 1) + 1; // 1 for the palindrome made by the two matching characters
    }
    
    // Count palindromic subsequences excluding either the start or end character
    count += countPalindromicSubsequences(str, start + 1, end); // excluding start
    count += countPalindromicSubsequences(str, start, end - 1); // excluding end
    count -= countPalindromicSubsequences(str, start + 1, end - 1); // subtracting the overlap, as it gets counted twice

    // Memoize the result
    memo[key] = count;
    return count;
}

int main() {
    string str = "abcadb"; // Example input
    int palindromicCount = countPalindromicSubsequences(str, 0, str.length() - 1);
    
    cout << "Number of palindromic subsequences: " << palindromicCount << endl;

    return 0;
}
