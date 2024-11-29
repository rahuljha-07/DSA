#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <vector>
#include <string>
using namespace std;

// Function to generate all possible one-letter transformations of a word
void wordMatch(const string& word, unordered_map<string, bool>& visited, queue<string>& q) {
    for (int i = 0; i < word.length(); i++) {
        // Convert the word to a mutable character array
        string tempWord = word;

        // Replace the character at position `i` with every letter 'a' to 'z'
        for (char c = 'a'; c <= 'z'; c++) {
            tempWord[i] = c;

            // If the transformed word is in the dictionary and not visited
            if (visited.find(tempWord) != visited.end() && !visited[tempWord]) {
                q.push(tempWord);          // Add the word to the queue for BFS
                visited[tempWord] = true; // Mark the word as visited
            }
        }
    }
}

// Function to find the shortest transformation sequence
int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
    // If endWord is not in the wordList, return 0
    unordered_set<string> wordSet(wordList.begin(), wordList.end());
    if (wordSet.find(endWord) == wordSet.end()) return 0;

    // Create a visited map to track visited words
    unordered_map<string, bool> visited;
    for (const string& word : wordList) {
        visited[word] = false;
    }

    // BFS initialization
    queue<string> q;
    q.push(beginWord);
    visited[beginWord] = true;
    int length = 1; // Length of the transformation sequence

    // Perform BFS
    while (!q.empty()) {
        int size = q.size(); // Number of elements in the current level

        for (int i = 0; i < size; i++) {
            string currentWord = q.front();
            q.pop();

            // If the endWord is found, return the length of the sequence
            if (currentWord == endWord) {
                return length;
            }

            // Generate all valid transformations of the current word
            wordMatch(currentWord, visited, q);
        }

        // Increment the transformation length for the next level
        length++;
    }

    // If BFS completes without finding the endWord, return 0
    return 0;
}

int main() {
    // Example 1
    string beginWord1 = "hit";
    string endWord1 = "cog";
    vector<string> wordList1 = {"hot", "dot", "dog", "lot", "log", "cog"};
    cout << "Output: " << ladderLength(beginWord1, endWord1, wordList1) << endl; // Output: 5

    // Example 2
    string beginWord2 = "hit";
    string endWord2 = "cog";
    vector<string> wordList2 = {"hot", "dot", "dog", "lot", "log"};
    cout << "Output: " << ladderLength(beginWord2, endWord2, wordList2) << endl; // Output: 0

    return 0;
}
