#include <iostream>
#include <vector>
#include <string>
using namespace std;

class TrieNode {
public:
    TrieNode* children[26] = {};
    int frequency = 0; // Frequency to track occurrences of each prefix
};

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();
    }

    // Insert a word into the Trie and update frequency count for each node
    void insert(const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            int index = c - 'a';
            if (node->children[index] == nullptr) {
                node->children[index] = new TrieNode();
            }
            node = node->children[index];
            node->frequency++;
        }
    }

    // Find shortest unique prefix for a given word
    string getUniquePrefix(const string& word) {
        TrieNode* node = root;
        string prefix;
        for (char c : word) {
            int index = c - 'a';
            node = node->children[index];
            prefix += c;
            // Check if this node's frequency is 1, meaning this path is unique
            if (node->frequency == 1) {
                return prefix;
            }
        }
        return prefix; // If no unique prefix, return the whole word
    }
};

// Function to find shortest unique prefixes for all words in the array
vector<string> findUniquePrefixes(const vector<string>& words) {
    Trie trie;
    for (const string& word : words) {
        trie.insert(word); // Insert each word into the Trie
    }

    vector<string> uniquePrefixes;
    for (const string& word : words) {
        uniquePrefixes.push_back(trie.getUniquePrefix(word)); // Find each word's unique prefix
    }
    return uniquePrefixes;
}

int main() {
    vector<string> words1 = {"zebra", "dog", "duck", "dove"};
    vector<string> result1 = findUniquePrefixes(words1);
    for (const string& prefix : result1) {
        cout << prefix << " ";
    }
    cout << endl;

    vector<string> words2 = {"geeksgeeks", "geeksquiz", "geeksforgeeks"};
    vector<string> result2 = findUniquePrefixes(words2);
    for (const string& prefix : result2) {
        cout << prefix << " ";
    }
    cout << endl;

    return 0;
}

/*
Let's go through how the Trie helps us find the shortest unique prefix for each word in the list `{"zebra", "dog", "duck", "dove"}`.

### Step-by-Step Explanation of the Trie Approach

1. **Insert Each Word into the Trie**:  
   - As each word is inserted, the Trie nodes keep track of how many times each prefix appears by incrementing a frequency counter in each node. This helps us know if a prefix is unique.

2. **Finding the Shortest Unique Prefix**:
   - For each word, we start from the root of the Trie and traverse down its letters.
   - At each node, we check the frequency of that node.
   - The first time we find a node with `frequency == 1`, it means that the path to that node is unique to this word. Thus, the letters we've traversed so far form the shortest unique prefix.

Let’s walk through each word in `{"zebra", "dog", "duck", "dove"}`:

### Word-by-Word Breakdown

#### 1. Insert "zebra" into the Trie
   - For each character in "zebra":
      - `z`: A new node for `z` is created, and its frequency is set to 1.
      - `e`: A new node for `e` is created, and its frequency is set to 1.
      - `b`: A new node for `b` is created, and its frequency is set to 1.
      - `r`: A new node for `r` is created, and its frequency is set to 1.
      - `a`: A new node for `a` is created, and its frequency is set to 1.
   - After inserting "zebra", each node along this path has a frequency of 1 because no other word has the same prefix.

#### 2. Insert "dog" into the Trie
   - For each character in "dog":
      - `d`: A new node for `d` is created, and its frequency is set to 1.
      - `o`: A new node for `o` is created, and its frequency is set to 1.
      - `g`: A new node for `g` is created, and its frequency is set to 1.
   - After inserting "dog", each node along this path has a frequency of 1 because no other word has the same prefix.

#### 3. Insert "duck" into the Trie
   - For each character in "duck":
      - `d`: This node already exists from "dog", so we move to it and increment its frequency to 2.
      - `u`: A new node for `u` is created, and its frequency is set to 1.
      - `c`: A new node for `c` is created, and its frequency is set to 1.
      - `k`: A new node for `k` is created, and its frequency is set to 1.

#### 4. Insert "dove" into the Trie
   - For each character in "dove":
      - `d`: This node already exists, so we increment its frequency to 3.
      - `o`: This node already exists, so we increment its frequency to 2.
      - `v`: A new node for `v` is created, and its frequency is set to 1.
      - `e`: A new node for `e` is created, and its frequency is set to 1.

### Finding the Shortest Unique Prefix

Now, let’s find the shortest unique prefix for each word by checking the frequency at each node.

1. **"zebra"**:
   - Starting at the root, go down to `z`. The node for `z` has a frequency of 1, which means that "z" is already unique for "zebra". Therefore, the shortest unique prefix for "zebra" is `"z"`.

2. **"dog"**:
   - Starting at the root, go down to `d`. The node for `d` has a frequency of 3, so `d` alone is not unique.
   - Move to `o`. The node for `o` has a frequency of 2, so `do` is also not unique.
   - Move to `g`. The node for `g` has a frequency of 1, making `dog` unique.
   - Thus, the shortest unique prefix for "dog" is `"dog"`.

3. **"duck"**:
   - Starting at the root, go down to `d`. The node for `d` has a frequency of 3, so `d` alone is not unique.
   - Move to `u`. The node for `u` has a frequency of 1, so `du` is unique for "duck".
   - Thus, the shortest unique prefix for "duck" is `"du"`.

4. **"dove"**:
   - Starting at the root, go down to `d`. The node for `d` has a frequency of 3, so `d` alone is not unique.
   - Move to `o`. The node for `o` has a frequency of 2, so `do` is also not unique.
   - Move to `v`. The node for `v` has a frequency of 1, so `dov` is unique for "dove".
   - Thus, the shortest unique prefix for "dove" is `"dov"`.

### Final Result

The shortest unique prefixes for the words are:
- **"zebra"**: `"z"`
- **"dog"**: `"dog"`
- **"duck"**: `"du"`
- **"dove"**: `"dov"`

This approach ensures each prefix is the shortest possible string that can distinguish each word from all others in the list.
*/