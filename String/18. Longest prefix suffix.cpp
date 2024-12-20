// same as build lps in kmp algo
// just found the largest value at end
#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> buildPrefixTable(const string& str) {
    int n = str.size();
    vector<int> prefixTable(n, 0);
    int j = 0; // Length of the previous longest prefix suffix

    // Build the prefix table
    for (int i = 1; i < n; i++) {
        while (j > 0 && str[i] != str[j]) {
            j = prefixTable[j - 1]; // Fallback in the prefix table
        }
        if (str[i] == str[j]) {
            j++;
        }
        prefixTable[i] = j; // Update the prefix table
    }

    return prefixTable[n-1];
}

int longestPrefixSuffix(const string& str) {
    return buildPrefixTable(str);
}

int main() {
    string str1 = "abab";
    string str2 = "aaaa";
    
    cout << "Longest Prefix Suffix length for '" << str1 << "': " << longestPrefixSuffix(str1) << endl;
    cout << "Longest Prefix Suffix length for '" << str2 << "': " << longestPrefixSuffix(str2) << endl;

    return 0;
}
