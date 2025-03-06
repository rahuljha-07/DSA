#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

// Function to check if two strings are isomorphic
bool areIsomorphic(const string& str1, const string& str2) {
    if (str1.length() != str2.length()) return false; // Check if lengths are equal

    unordered_map<char, char> mapping1, mapping2; // Maps for tracking character mappings

    for (int i = 0; i < str1.length(); i++) {
        // Check if the current character from str1 has already been mapped to a different character in str2
        // If it has a mapping and it does not match the current character in str2, return false
        if (mapping1[str1[i]] && mapping1[str1[i]] != str2[i]) return false; 
        mapping1[str1[i]] = str2[i]; // Map the current character from str1 to the corresponding character in str2

        // Check if the current character from str2 has already been mapped to a different character in str1
        // If it has a mapping and it does not match the current character in str1, return false
        if (mapping2[str2[i]] && mapping2[str2[i]] != str1[i]) return false; 
        mapping2[str2[i]] = str1[i]; // Map the current character from str2 to the corresponding character in str1
    }

    return true; // All mappings are consistent, return true
}

int main() {
    cout << "Are 'paper' and 'title' isomorphic? " << (areIsomorphic("paper", "title") ? "Yes" : "No") << endl;
    cout << "Are 'foo' and 'bar' isomorphic? " << (areIsomorphic("foo", "bar") ? "Yes" : "No") << endl;

    return 0;
}
