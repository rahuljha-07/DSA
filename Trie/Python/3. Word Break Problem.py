class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:
    # Constructor to initialize the Trie
    def __init__(self):
        # Create the root node
        self.root = TrieNode()

    # Insert a word into the Trie
    def insert(self, word):
        node = self.root
        for c in word:
            # Convert char to index (0 for 'a', 1 for 'b', ..., 25 for 'z')
            index = ord(c) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        # Mark the end of the word
        node.isEndOfWord = True

    # Search for a word in the Trie
    def search(self, word):
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                # If a character does not exist, return false
                return False
            node = node.children[index]
        # Return true if it's the end of the word
        return node.isEndOfWord

    # Check if a prefix exists in the Trie
    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                # If a prefix does not exist, return false
                return False
            node = node.children[index]
        return True


# Word Break without DP using recursion
def wordBreakRecursive(s, trie, start):
    if start == len(s):
        # If we've processed the entire string, return true
        return True
    # Try all possible prefixes starting from the current position
    for end in range(start + 1, len(s) + 1):
        prefix = s[start:end]
        if trie.search(prefix):
            # If the prefix exists in the Trie, recursively check the remaining part of the
            # string
            if wordBreakRecursive(s, trie, end):
                # If we can segment the rest of the string, return true
                return True
    # If no valid segmentation is found
    return False


def main():
    dictionary = ["i", "like", "sam", "sung", "samsung", "mobile", "ice",
                  "cream", "icecream", "man", "go", "mango"]
    trie = Trie()
    for word in dictionary:
        trie.insert(word)
    test1 = "ilike"
    test2 = "ilikesamsung"
    print("Test 1:", "Yes" if wordBreakRecursive(test1, trie, 0) else "No")
    print("Test 2:", "Yes" if wordBreakRecursive(test2, trie, 0) else "No")


if __name__ == "__main__":
    main()


'''
Let n be string length and T total dictionary characters.
Time: O(T + n^2 * 2^n) conservative worst-case bound: there can be
exponentially many segmentation attempts without memoization, and each
call scans possible ends, copying/searching prefixes in up to O(n^2).
Space: O(T + n) auxiliary trie, recursion, and retained prefix strings:
the chosen prefixes along an active call path partition at most n characters.
Early success can avoid much of this work; the recursive approach is retained.
'''
