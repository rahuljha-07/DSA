#include <string>
using namespace std;

class TriNode {
public:
    TriNode* children[26] = {nullptr};
    bool isEnd = false;
};

class Trie {
public:
    TriNode* root;

    Trie() {
        root = new TriNode();
    }

    void insert(string word) {
        TriNode* node = root;
        for (char c : word) {
            if (node->children[c - 'a'] == nullptr) {
                node->children[c - 'a'] = new TriNode();
            }
            node = node->children[c - 'a'];
        }
        node->isEnd = true;
    }

    bool search(string word) {
        TriNode* node = root;
        for (char c : word) {
            if (node->children[c - 'a'] == nullptr)
                return false;
            node = node->children[c - 'a'];
        }
        return node->isEnd;
    }

    bool startsWith(string prefix) {
        TriNode* node = root;
        for (char c : prefix) {
            if (node->children[c - 'a'] == nullptr)
                return false;
            node = node->children[c - 'a'];
        }
        return true;
    }

    bool deleteWord(string word) {
        return deleteHelper(root, word, 0);
    }

private:
    bool deleteHelper(TriNode* node, const string& word, int depth) {
        if (!node) return false;

        // Base case: if end of word is reached
        if (depth == word.size()) {
            if (!node->isEnd) return false; // Word not present

            node->isEnd = false; // Unmark the end of the word
            return isEmpty(node); // Check if node has any children
        }

        int index = word[depth] - 'a';
        if (!deleteHelper(node->children[index], word, depth + 1)) return false;

        // If child node can be deleted, remove it
        delete node->children[index];
        node->children[index] = nullptr;

        // Return true if current node has no children and is not end of another word
        return !node->isEnd && isEmpty(node);
    }

    bool isEmpty(TriNode* node) {
        for (int i = 0; i < 26; i++) {
            if (node->children[i]) return false;
        }
        return true;
    }
};
