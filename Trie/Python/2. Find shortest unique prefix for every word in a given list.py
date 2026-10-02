class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.frequency = 0


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
            node.frequency += 1

    def getUniquePrefix(self, word):
        node = self.root
        prefix = ""
        for c in word:
            index = ord(c) - ord('a')
            node = node.children[index]
            prefix += c
            if node.frequency == 1:
                return prefix
        return prefix


def findUniquePrefixes(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    uniquePrefixes = []
    for word in words:
        uniquePrefixes.append(trie.getUniquePrefix(word))
    return uniquePrefixes


def main():
    words1 = ["zebra", "dog", "duck", "dove"]
    result1 = findUniquePrefixes(words1)
    print(*result1)
    words2 = ["geeksgeeks", "geeksquiz", "geeksforgeeks"]
    result2 = findUniquePrefixes(words2)
    print(*result2)


if __name__ == "__main__":
    main()


'''
Let T be total word characters and Li each word's length.
Time: O(T) trie traversal/insertion work. Building growing prefix strings
can conservatively add O(sum(Li^2)) copying if appends are not optimized.
Space: O(T) auxiliary trie storage plus output prefixes of at most O(T).
Alphabet size is fixed at 26. Inputs should have unique prefixes; if a
word repeats or prefixes another word, the source returns its full text
even when that text is not a unique prefix.
'''
