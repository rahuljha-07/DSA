import sys


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.contactList = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, contact):
        node = self.root
        for c in contact:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
            node.contactList.append(contact)

    def getContactsByPrefix(self, prefix):
        node = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                return []
            node = node.children[index]
        node.contactList.sort()
        return list(node.contactList)


def main():
    tokens = iter(sys.stdin.read().split())
    n = int(next(tokens))
    contact = [next(tokens) for _ in range(n)]
    query = next(tokens)
    trie = Trie()
    for contact_str in contact:
        trie.insert(contact_str)
    for i in range(1, len(query) + 1):
        prefix = query[:i]
        result = trie.getContactsByPrefix(prefix)
        print(*result) if result else print("0")


if __name__ == "__main__":
    main()


'''
Let T be total contact characters, Q query length, and ci matches for
query prefix i. Insertion is O(T): store one reference at each prefix node.
Time: a prefix lookup costs O(i + ci log(ci+1)) comparisons plus O(ci)
result copying; string comparisons can cost up to the longest contact
length L. All Q lookups cost O(Q^2 + sum(ci log(ci+1)*L)), plus printing.
Space: O(T) trie nodes/contact references (Python reuses contact strings),
plus O(max ci) query result/sorting workspace. Results retain duplicates
and return copies, matching C++ value-return semantics.
'''
