#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
using namespace std;

class TrieNode {
public:
    TrieNode* children[26] = {nullptr};  // Array to store child nodes for each letter a-z
    vector<string> contactList;    // To store contacts that pass through this node
};

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();
    }

    // Insert a contact into the Trie
    void insert(const string& contact) {
        TrieNode* node = root;
        for (char c : contact) {
            int index = c - 'a';
            if (node->children[index] == nullptr) {
                node->children[index] = new TrieNode();
            }
            node = node->children[index];
            node->contactList.push_back(contact);  // Add contact to the contact list of the current node
        }
    }

    // Function to retrieve all contacts that start with the given prefix
    vector<string> getContactsByPrefix(const string& prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            int index = c - 'a';
            if (node->children[index] == nullptr) {
                return {};  // Return empty if no contacts match the prefix
            }
            node = node->children[index];
        }
        // Sort the contacts for the given prefix in lexicographical order
        sort(node->contactList.begin(), node->contactList.end());
        return node->contactList;
    }
};

int main() {
    int n;
    cin >> n;
    vector<string> contact(n);
    for (int i = 0; i < n; i++) {
        cin >> contact[i];
    }
    string query;
    cin >> query;

    // Create a Trie and insert all contacts
    Trie trie;
    for (const string& contact_str : contact) {
        trie.insert(contact_str);
    }

    // For each prefix of the query string, get the matching contacts
    for (int i = 1; i <= query.length(); ++i) {
        string prefix = query.substr(0, i);
        vector<string> result = trie.getContactsByPrefix(prefix);

        if (result.empty()) {
            cout << "0" << endl;  // No contacts found for this prefix
        } else {
            for (const string& contact : result) {
                cout << contact << " ";
            }
            cout << endl;
        }
    }

    return 0;
}

/*
Let's walk through the **insert** process in detail, step by step, using an example. We'll focus on how each character in the contact is inserted into the Trie, how new nodes are created if needed, and how the contact is added to the `contactList` of the corresponding nodes.

### **Example Contact List**:
Let's say we have the following contact list:
```
["geeikistest", "geeksforgeeks", "geeksfortest"]
```

We will insert these contacts one by one into the Trie, so let's focus on the first contact, `"geeikistest"`.

### **Step 1: Initialize the Trie**
The Trie starts with an empty root node. The root node has an array of 26 `children` (for each letter from 'a' to 'z'), all initially set to `nullptr`. This array represents the possible next characters for the Trie nodes.

```cpp
class TrieNode {
public:
    TrieNode* children[26] = {};  // Array to store children nodes for characters a-z
    vector<string> contactList;    // To store contacts passing through this node
};
```

- The **root node** starts as follows:
  - `children[26]`: All `nullptr` initially.
  - `contactList`: Empty initially.

### **Step 2: Insert "geeikistest"**
We will insert the contact `"geeikistest"` into the Trie character by character:

1. **Insert 'g'**:
   - Start at the root node.
   - The root node doesn't have a child for `'g'` (`children['g' - 'a']` is `nullptr`), so we create a new Trie node for `'g'`.
   - Move to this new node and add the contact `"geeikistest"` to its `contactList`.

2. **Insert 'e'**:
   - Now, at the `'g'` node, we look for a child for `'e'`.
   - The `'g'` node doesn't have a child for `'e'` (`children['e' - 'a']` is `nullptr`), so we create a new Trie node for `'e'`.
   - Move to this new node and add the contact `"geeikistest"` to its `contactList`.

3. **Insert 'e'** (again):
   - Now, at the `'e'` node, we look for a child for `'e'`.
   - The `'e'` node doesn't have a child for `'e'` (`children['e' - 'a']` is `nullptr`), so we create a new Trie node for `'e'`.
   - Move to this new node and add the contact `"geeikistest"` to its `contactList`.

4. **Insert 'i'**:
   - Now, at the `'e'` node, we look for a child for `'i'`.
   - The `'e'` node doesn't have a child for `'i'` (`children['i' - 'a']` is `nullptr`), so we create a new Trie node for `'i'`.
   - Move to this new node and add the contact `"geeikistest"` to its `contactList`.

5. **Insert 'k'**:
   - Now, at the `'i'` node, we look for a child for `'k'`.
   - The `'i'` node doesn't have a child for `'k'` (`children['k' - 'a']` is `nullptr`), so we create a new Trie node for `'k'`.
   - Move to this new node and add the contact `"geeikistest"` to its `contactList`.

6. **Insert 'i'**:
   - Now, at the `'k'` node, we look for a child for `'i'`.
   - The `'k'` node doesn't have a child for `'i'` (`children['i' - 'a']` is `nullptr`), so we create a new Trie node for `'i'`.
   - Move to this new node and add the contact `"geeikistest"` to its `contactList`.

7. **Insert 's'**:
   - Now, at the `'i'` node, we look for a child for `'s'`.
   - The `'i'` node doesn't have a child for `'s'` (`children['s' - 'a']` is `nullptr`), so we create a new Trie node for `'s'`.
   - Move to this new node and add the contact `"geeikistest"` to its `contactList`.

8. **Insert 't'**:
   - Now, at the `'s'` node, we look for a child for `'t'`.
   - The `'s'` node doesn't have a child for `'t'` (`children['t' - 'a']` is `nullptr`), so we create a new Trie node for `'t'`.
   - Move to this new node and add the contact `"geeikistest"` to its `contactList`.

9. **Insert 'e'**:
   - Now, at the `'t'` node, we look for a child for `'e'`.
   - The `'t'` node doesn't have a child for `'e'` (`children['e' - 'a']` is `nullptr`), so we create a new Trie node for `'e'`.
   - Move to this new node and add the contact `"geeikistest"` to its `contactList`.

10. **Insert 's'**:
    - Now, at the `'e'` node, we look for a child for `'s'`.
    - The `'e'` node doesn't have a child for `'s'` (`children['s' - 'a']` is `nullptr`), so we create a new Trie node for `'s'`.
    - Move to this new node and add the contact `"geeikistest"` to its `contactList`.

11. **Insert 't'**:
    - Now, at the `'s'` node, we look for a child for `'t'`.
    - The `'s'` node doesn't have a child for `'t'` (`children['t' - 'a']` is `nullptr`), so we create a new Trie node for `'t'`.
    - Move to this new node and add the contact `"geeikistest"` to its `contactList`.

At this point, the contact `"geeikistest"` has been completely inserted into the Trie. The `contactList` of every node traversed during the insertion of `"geeikistest"` contains this contact.

### **Step 3: Inserting "geeksforgeeks"**
Now, let's insert `"geeksforgeeks"` into the Trie.

1. **Insert 'g'**:
   - We start at the root. The root already has a child for `'g'`, so we move to that node. No new node is created.
   
2. **Insert 'e'**:
   - The `'g'` node already has a child for `'e'`, so we move to that node. No new node is created.

3. **Insert 'e'**:
   - The `'e'` node already has a child for `'e'`, so we move to that node. No new node is created.

4. **Insert 'k'**:
   - The `'e'` node already has a child for `'k'`, so we move to that node. No new node is created.

5. **Insert 's'**:
   - The `'k'` node already has a child for `'s'`, so we move to that node. No new node is created.

6. **Insert 'f'**:
   - The `'s'` node doesn't have a child for `'f'`, so we create a new node for `'f'`.

7. **Insert 'o'**:
   - The `'f'` node doesn't have a child for `'o'`, so we create a new node for `'o'`.

8. **Insert 'r'**:
   - The `'o'` node doesn't have a child for `'r'`, so we create a new node for `'r'`.

9. **Insert 'g'**:
   - The `'r'` node doesn't have a child for `'g'`, so we create a new node for `'g'`.

10. **Insert 'e'**:
    - The `'g'` node doesn't have a child for `'e'`, so we create a new node for `'e'`.

11. **Insert 'e'**:
    - The `'e'` node doesn't have a child for `'e'`, so we create a new node for `'e'`.

12. **Insert 'k'**:
    - The `'e'` node doesn't have a child for `'k'`, so we create a new node for `'k'`.

13. **Insert 's'**:
    - The `'k'` node doesn't have a child for `'s'`, so we create a new node for `'s'`.

Now the contact `"geeksforgeeks"` is fully inserted into the Trie, and the `contactList` at each relevant node will contain `"geeksforgeeks"`.

### **Result After Insertion of All Contacts**
After inserting all three contacts, the Trie structure will contain nodes corresponding to each prefix, and the `contactList` at each node will contain the contact(s) that pass through that node.

### **Summary of Insert Process**:
- The insert process for a contact works by following each character in the contact and navigating through or creating new Trie nodes.


- Each node keeps track of contacts that pass through it, and the `contactList` is updated as we traverse through the nodes.

This Trie structure helps efficiently handle the prefix-based search queries in the **Phone Directory Problem**, as shown in the previous walkthroughs.

Trie Structure:
Root
  |
  g (contactList: ["geeikistest", "geeksforgeeks", "geeksfortest"])
  |
  e (contactList: ["geeikistest", "geeksforgeeks", "geeksfortest"])
  |
  e (contactList: ["geeikistest", "geeksforgeeks", "geeksfortest"])
  |
  i (contactList: ["geeikistest"])
  |
  k (contactList: ["geeikistest"])
  |
  i (contactList: ["geeikistest"])
  |
  s (contactList: ["geeikistest"])
  |
  t (contactList: ["geeikistest"])
  |
  e (contactList: ["geeikistest"])
  |
  s (contactList: ["geeikistest"])
  |
  t (contactList: ["geeikistest"])
  
  ───────────────────────────────────────────────────────────────
  
  e (contactList: ["geeksforgeeks", "geeksfortest"])
  |
  k (contactList: ["geeksforgeeks", "geeksfortest"])
  |
  s (contactList: ["geeksforgeeks", "geeksfortest"])
  |
  f (contactList: ["geeksforgeeks"])
  |
  o (contactList: ["geeksforgeeks"])
  |
  r (contactList: ["geeksforgeeks"])
  |
  g (contactList: ["geeksforgeeks"])
  |
  e (contactList: ["geeksforgeeks"])
  |
  e (contactList: ["geeksforgeeks"])
  |
  k (contactList: ["geeksforgeeks"])
  |
  s (contactList: ["geeksforgeeks"])

  ───────────────────────────────────────────────────────────────

  e (contactList: ["geeksfortest"])
  |
  f (contactList: ["geeksfortest"])
  |
  o (contactList: ["geeksfortest"])
  |
  r (contactList: ["geeksfortest"])
  |
  t (contactList: ["geeksfortest"])
  |
  e (contactList: ["geeksfortest"])
  |
  s (contactList: ["geeksfortest"])

*/