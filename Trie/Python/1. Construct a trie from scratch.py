class TriNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TriNode()

    def insert(self, word):
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                node.children[index] = TriNode()
            node = node.children[index]
        node.isEnd = True

    def search(self, word):
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                return False
            node = node.children[index]
        return node.isEnd

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                return False
            node = node.children[index]
        return True

    def deleteWord(self, word):
        return self.deleteHelper(self.root, word, 0)

    def deleteHelper(self, node, word, depth):
        if not node:
            return False
        # Base case: if end of word is reached
        if depth == len(word):
            if not node.isEnd:
                return False
            # Unmark the end of the word
            node.isEnd = False
            # Check if node has any children
            return self.isEmpty(node)
        index = ord(word[depth]) - ord('a')
        if not self.deleteHelper(node.children[index], word, depth + 1):
            return False
        # If child node can be deleted, remove it
        node.children[index] = None
        # Return true if current node has no children and is not end of another word
        return not node.isEnd and self.isEmpty(node)

    def isEmpty(self, node):
        for i in range(26):
            if node.children[i]:
                return False
        return True


'''
Let L be word/prefix length and T the total inserted character count.
Time: O(L) per insert/search/startsWith/deleteWord: one child lookup per
character. Deletion also scans 26 children per level, a constant alphabet.
Space: O(T) trie storage worst case; insertion adds at most O(L) nodes.
Search/prefix checking use O(1) auxiliary space; deletion uses O(L) stack.
Lowercase a-z inputs are required. As in C++, deleteWord's bool means
the root is now prunable, NOT simply that deletion succeeded.
'''
