#include <iostream>
#include <unordered_map>
#include <queue>
#include <vector>
#include <string>
using namespace std;

// Function to return a vector of first non-repeating characters in a stream
vector<string> getFirstNonRepeatingCharactersInStream(char stream[], int n) {
    unordered_map<char, int> charCount; // Map to store character frequencies
    queue<char> q;                      // Queue to track first non-repeating characters
    vector<string> result;              // Vector to store the result

    // Process each character in the stream
    for (int i = 0; i < n; i++) {
        char currentChar = stream[i];
        
        // Update the frequency of the current character
        charCount[currentChar]++;
        
        // If the character appears for the first time, add it to the queue
        if (charCount[currentChar] == 1) {
            q.push(currentChar);
        }

        // Check the front of the queue to find the first non-repeating character
        while (!q.empty()) {
            char frontChar = q.front();
            if (charCount[frontChar] == 1) {
                // If the front character is non-repeating, keep it in the queue
                break;
            } else {
                // If the front character is repeating, remove it
                q.pop();
            }
        }

        // Add the first non-repeating character to the result vector or "#" if none
        if (q.empty()) {
            result.push_back("#"); // No non-repeating character
        } else {
            result.push_back(string(1, q.front())); // Convert char to string
        }
    }

    return result;
}

// Main function to test the code
int main() {
    char stream[] = {'a', 'b', 'c', 'a', 'c', 'b', 'd'};
    int n = sizeof(stream) / sizeof(stream[0]);

    vector<string> result = getFirstNonRepeatingCharactersInStream(stream, n);

    // Print the result vector
    for (const string& s : result) {
        cout << s << " ";
    }
    cout << endl;

    return 0;
}
