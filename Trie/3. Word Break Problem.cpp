#include <iostream>
#include <unordered_set>
#include <vector>
#include <string>
using namespace std;

// Define the TrieNode class
class TrieNode {
public:
    TrieNode* children[26] = {nullptr};  // Array to store child nodes (one for each letter)
    bool isEndOfWord = false;  // Mark the end of a word
};

// Define the Trie class
class Trie {
public:
    TrieNode* root;

    // Constructor to initialize the Trie
    Trie() {
        root = new TrieNode();  // Create the root node
    }

    // Insert a word into the Trie
    void insert(const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            int index = c - 'a';  // Convert char to index (0 for 'a', 1 for 'b', ..., 25 for 'z')
            if (node->children[index] == nullptr) {
                node->children[index] = new TrieNode();
            }
            node = node->children[index];
        }
        node->isEndOfWord = true;  // Mark the end of the word
    }

    // Search for a word in the Trie
    bool search(const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            int index = c - 'a';
            if (node->children[index] == nullptr) {
                return false;  // If a character does not exist, return false
            }
            node = node->children[index];
        }
        return node->isEndOfWord;  // Return true if it's the end of the word
    }

    // Check if a prefix exists in the Trie
    bool startsWith(const string& prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            int index = c - 'a';
            if (node->children[index] == nullptr) {
                return false;  // If a prefix does not exist, return false
            }
            node = node->children[index];
        }
        return true;
    }
};

// Word Break without DP using recursion
bool wordBreakRecursive(const string& s, Trie& trie, int start) {
    if (start == s.length()) {
        return true;  // If we've processed the entire string, return true
    }

    // Try all possible prefixes starting from the current position
    for (int end = start + 1; end <= s.length(); ++end) {
        string prefix = s.substr(start, end - start);
        if (trie.search(prefix)) {
            // If the prefix exists in the Trie, recursively check the remaining part of the string
            if (wordBreakRecursive(s, trie, end)) {
                return true;  // If we can segment the rest of the string, return true
            }
        }
    }

    return false;  // If no valid segmentation is found
}

int main() {
    vector<string> dictionary = {"i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"};
    Trie trie;
    
    // Insert all words in the dictionary into the Trie
    for (const string& word : dictionary) {
        trie.insert(word);
    }

    // Test cases
    string test1 = "ilike";
    string test2 = "ilikesamsung";
    
    cout << "Test 1: " << (wordBreakRecursive(test1, trie, 0) ? "Yes" : "No") << endl;
    cout << "Test 2: " << (wordBreakRecursive(test2, trie, 0) ? "Yes" : "No") << endl;

    return 0;
}
