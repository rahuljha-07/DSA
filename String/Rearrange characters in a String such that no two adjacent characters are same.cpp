#include <iostream>
#include <string>
#include <unordered_map>
#include <queue>
#include <vector>

using namespace std;

// Function to rearrange characters in a string so that no two adjacent characters are the same
string rearrangeString(string s) {
    // Create a frequency map to count occurrences of each character
    unordered_map<char, int> charCount;
    for (char c : s) {
        charCount[c]++;
    }

    // Create a max heap based on character frequencies
    priority_queue<pair<int, char>> maxHeap;
    for (const auto& entry : charCount) {
        maxHeap.push({entry.second, entry.first});
    }

    // Check the condition for possibility
    int n = s.length();
    if (maxHeap.top().first > (n + 1) / 2) {
        return "Not Possible"; // If the most frequent character's count is greater than half of the string length
    }

    string result;
    // Create a vector to store the characters while maintaining the odd/even index filling
    vector<char> resultVec(n);
    int index = 0;

    // Fill characters in the result
    while (!maxHeap.empty()) {
        auto [count, char] = maxHeap.top(); // Get the character with the highest frequency
        maxHeap.pop();

        // Place the character in the result
        for (int i = 0; i < count; i++) {
            if (index >= n) {
                index = 1; // Move to odd index after filling even indices
            }
            resultVec[index] = char; // Place character at the current index
            index += 2; // Increment index to fill the next position
        }
    }

    // Convert the vector back to a string
    return string(resultVec.begin(), resultVec.end());
}

// Example usage
int main() {
    string input1 = "aaabc";
    cout << "Input: " << input1 << ", Output: " << rearrangeString(input1) << endl; // Output: abaca

    string input2 = "aaabb";
    cout << "Input: " << input2 << ", Output: " << rearrangeString(input2) << endl; // Output: ababa

    string input3 = "aa";
    cout << "Input: " << input3 << ", Output: " << rearrangeString(input3) << endl; // Output: Not Possible

    string input4 = "aaaabc";
    cout << "Input: " << input4 << ", Output: " << rearrangeString(input4) << endl; // Output: Not Possible

    return 0;
}
