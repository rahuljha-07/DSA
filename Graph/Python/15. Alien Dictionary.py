# Helper function to perform DFS and store nodes in topological order
def topoSortUtil(node, adj, visited, topoStack):
    # Mark the node as visited
    visited[node] = True
    # Explore all neighbors
    for neighbor in adj[node]:
        if not visited[neighbor]:
            topoSortUtil(neighbor, adj, visited, topoStack)
    # Push the node into the stack after exploring all its neighbors
    topoStack.append(node)


# Function to perform topological sorting
def topologicalSort(adj, K):
    # To track visited nodes
    visited = [False] * K
    # Stack to store topological order
    topoStack = []
    # Perform DFS for all unvisited nodes
    for i in range(K):
        if not visited[i]:
            topoSortUtil(i, adj, visited, topoStack)
    # Extract nodes from the stack to get the topological order
    topoOrder = ""
    while topoStack:
        topoOrder += chr(ord('a') + topoStack.pop())
    return topoOrder


# Function to build the graph based on the given words
def buildGraph(words, N, K):
    # Graph with K nodes (representing the alphabet)
    adj = [[] for _ in range(K)]
    for i in range(N - 1):
        word1 = words[i]
        word2 = words[i + 1]
        if len(word1) > len(word2) and word1[:len(word2)] == word2:
            # Return an empty graph indicating an invalid input
            return []
        # Compare characters of both words
        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                # Character index in the alphabet
                index1 = ord(word1[j]) - ord('a')
                index2 = ord(word2[j]) - ord('a')
                # Add a directed edge
                adj[index1].append(index2)
                # Only the first differing character determines the order
                break
    return adj


# Function to find the order of characters in the alien dictionary
def findOrder(words, N, K):
    adj = buildGraph(words, N, K)
    # Check for invalid graph (prefix issue)
    if not adj:
        return "Invalid input (prefix ordering issue)."
    # Perform topological sort to find the order of characters
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
