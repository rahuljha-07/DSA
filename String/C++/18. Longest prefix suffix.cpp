#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> buildPrefixTable(const string& str) {
    int n = str.size();
    vector<int> prefixTable(n, 0);
    int j = 0; // Length of the previous longest prefix suffix

    for (int i = 1; i < n; i++) {
        while (j > 0 && str[i] != str[j]) {
            j = prefixTable[j - 1]; // Fallback
        }
        if (str[i] == str[j]) {
            j++;
        }
        prefixTable[i] = j; // Update table
    }

    return prefixTable; // Return full table instead of last value
}

int longestPrefixSuffix(const string& str) {
    vector<int> prefixTable = buildPrefixTable(str);

    // Find the max value in the prefix table
    int maxLPS = 0;
    for (int i = 0; i < prefixTable.size(); i++) {
        maxLPS = max(maxLPS, prefixTable[i]);
    }

    return maxLPS;
}

int main() {
    string str1 = "abab";
    string str2 = "aaaa";
    string str3 = "abcdabc";
    string str4 = "abcab";
    
    cout << "Longest Prefix Suffix length for '" << str1 << "': " << longestPrefixSuffix(str1) << endl;
    cout << "Longest Prefix Suffix length for '" << str2 << "': " << longestPrefixSuffix(str2) << endl;
    cout << "Longest Prefix Suffix length for '" << str3 << "': " << longestPrefixSuffix(str3) << endl;
    cout << "Longest Prefix Suffix length for '" << str4 << "': " << longestPrefixSuffix(str4) << endl;

    return 0;
}
