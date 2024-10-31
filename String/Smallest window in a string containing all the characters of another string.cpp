#include <unordered_map>
#include <string>
#include <limits.h>
using namespace std;

string minWindow(string s, string t) {
    // Frequency map for characters in t
    unordered_map<char, int> mp;
    for (auto ch : t) {
        mp[ch]++;
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
            // Update minimum window length and start index if needed
            if (mp.find(s[i]) != mp.end()) {
                mp[s[i]]++;
                if (mp[s[i]] == 1) {
                    count++; // We're missing this character now
                    // Update minimum length and start index
                    if (j - i + 1 < minLen) {
                        minLen = j - i + 1;
                        startIdx = i;
                    }
                }
            }
            i++; // Move the left pointer to contract the window
        }

        j++; // Expand the window by moving the right pointer
    }

    // If no valid window is found, return an empty string
    if (minLen == INT_MAX) return "";
    
    // Return the minimum window substring
    return s.substr(startIdx, minLen);
}
