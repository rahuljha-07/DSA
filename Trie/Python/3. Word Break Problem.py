class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.isEndOfWord = True

    def search(self, word):
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                return False
            node = node.children[index]
        return node.isEndOfWord

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                return False
            node = node.children[index]
        return True


def wordBreakRecursive(s, trie, start):
    if start == len(s):
        return True
    for end in range(start + 1, len(s) + 1):
        prefix = s[start:end]
        if trie.search(prefix):
            if wordBreakRecursive(s, trie, end):
                return True
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
