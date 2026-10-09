
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.contactList = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a contact into the Trie
    def insert(self, contact):
        node = self.root
        for c in contact:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
            # Add contact to the contact list of the current node
            node.contactList.append(contact)

    # Function to retrieve all contacts that start with the given prefix
    def getContactsByPrefix(self, prefix):
        node = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                # Return empty if no contacts match the prefix
                return []
            node = node.children[index]
        # Sort the contacts for the given prefix in lexicographical order
        node.contactList.sort()
        return list(node.contactList)


def main():
    n = int(input())
    contacts = input().split()
    query = input()

    trie = Trie()

    # Insert all contacts into the Trie
    for contact in contacts:
        trie.insert(contact)

    # Search contacts for every prefix of the query
    for i in range(1, len(query) + 1):
        prefix = query[:i]
        result = trie.getContactsByPrefix(prefix)

        if result:
            print(*result)
        else:
            print("0")


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
