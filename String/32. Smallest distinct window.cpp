#include <unordered_map>
#include <string>
#include <limits.h>
using namespace std;

string minWindow(string s) {
    // Frequency map for characters in t
    unordered_map<char, int> mp;
    for (auto ch : s) {
        mp[ch] = 1;
    }

    int minLen = INT_MAX; // Minimum length of the window found
    int startIdx = 0;     // Start index of the minimum window
    int i = 0;            // Left pointer for the sliding window
    int j = 0;            // Right pointer for the sliding window
    int count = mp.size(); // Number of unique characters in t

    while (j < s.length()) {
        // Decrease the count of the current character in the frequency map
        if (mp.find(s[j]) != mp.end()) {
            mp[s[j]]--;
            if (mp[s[j]] == 0) {
                count--; // Found a complete match for this character
            }
        }

        // Try to contract the window until it's no longer valid
        while (count == 0) {  
            // Update the minimum window before contracting
            if (j - i + 1 < minLen) {
                minLen = j - i + 1;
                startIdx = i;
            }
            // Try to remove s[i] and contract the window
            if (mp.find(s[i]) != mp.end()) {
                mp[s[i]]++;
                if (mp[s[i]] == 1) {  
                    count++;  // We lost a required character
                }
            }
            i++;  // Move left pointer to contract
        }
        j++; // Expand the window by moving the right pointer
    }

    // If no valid window is found, return an empty string
    if (minLen == INT_MAX) return "";
    
    // Return the minimum window substring
    return s.substr(startIdx, minLen);
}
