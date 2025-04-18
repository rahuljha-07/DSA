#include <bits/stdc++.h>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
using namespace std;

// Memoization map
unordered_map<string, unordered_set<string>> memo;

unordered_set<string> countPalindromicSubsequences(const string& str, int start, int end) {
    string key = to_string(start) + "_" + to_string(end);
    if (memo.find(key) != memo.end()) {
        return memo[key];
    }

    unordered_set<string> result;

    if (start > end) {
        return result;
    }

    if (start == end) {
        result.insert(string(1, str[start]));
        return result;
    }

    if (str[start] == str[end]) {
        unordered_set<string> innerSubseqs = countPalindromicSubsequences(str, start + 1, end - 1);
        for (const string& subseq : innerSubseqs) {
            result.insert(str[start] + subseq + str[end]);
        }
        result.insert(string(1, str[start]));
        result.insert(string(1, str[end]));
    }

    unordered_set<string> leftSubseqs = countPalindromicSubsequences(str, start + 1, end);
    unordered_set<string> rightSubseqs = countPalindromicSubsequences(str, start, end - 1);

    // Merge all results
    result.insert(leftSubseqs.begin(), leftSubseqs.end());
    result.insert(rightSubseqs.begin(), rightSubseqs.end());

    memo[key] = result;
    return result;
}

int main() {
    string str = "abcadb";
    unordered_set<string> palindromicSubsequences = countPalindromicSubsequences(str, 0, str.length() - 1);

    cout << "Number of palindromic subsequences: " << palindromicSubsequences.size() << endl;
    cout << "Palindromic Subsequences: ";
    for (const string& subseq : palindromicSubsequences) {
        cout << subseq << " ";
    }
    cout << endl;

    return 0;
}
