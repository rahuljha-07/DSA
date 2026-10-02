def topoSortUtil(node, adj, visited, topoStack):
    visited[node] = True
    for neighbor in adj[node]:
        if not visited[neighbor]:
            topoSortUtil(neighbor, adj, visited, topoStack)
    topoStack.append(node)


def topologicalSort(adj, K):
    visited = [False] * K
    topoStack = []
    for i in range(K):
        if not visited[i]:
            topoSortUtil(i, adj, visited, topoStack)
    topoOrder = ""
    while topoStack:
        topoOrder += chr(ord('a') + topoStack.pop())
    return topoOrder


def buildGraph(words, N, K):
    adj = [[] for _ in range(K)]
    for i in range(N - 1):
        word1 = words[i]
        word2 = words[i + 1]
        if len(word1) > len(word2) and word1[:len(word2)] == word2:
            return []
        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                index1 = ord(word1[j]) - ord('a')
                index2 = ord(word2[j]) - ord('a')
                adj[index1].append(index2)
                break
    return adj


def findOrder(words, N, K):
    adj = buildGraph(words, N, K)
    if not adj:
        return "Invalid input (prefix ordering issue)."
    return topologicalSort(adj, K)


def main():
    N = 5
    K = 4
    words = ["baa", "abcd", "abca", "cab", "cad"]
    order = findOrder(words, N, K)
    print("The order of characters in the alien dictionary:", order)


if __name__ == "__main__":
    main()


'''
Let T be total input characters, K alphabet size, and E constraints.
Time: O(T + K + E) traversal/comparison work: compare adjacent words
and DFS each letter/edge once. Building topoOrder may add O(K^2) string
copying if appends are not optimized (K<=26 makes this bounded).
Space: O(K + E) auxiliary graph, visited, and stacks; O(K) output.
Like the source, prefix conflicts are rejected but directed cycles are
not detected: input is otherwise assumed to admit a valid letter order.
'''
