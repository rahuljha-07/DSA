from collections import deque


def wordMatch(word, visited, q):
    for i in range(len(word)):
        tempWord = list(word)
        for c in "abcdefghijklmnopqrstuvwxyz":
            tempWord[i] = c
            candidate = "".join(tempWord)
            if candidate in visited and not visited[candidate]:
                q.append(candidate)
                visited[candidate] = True


def ladderLength(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    visited = {}
    for word in wordList:
        visited[word] = False
    q = deque([beginWord])
    visited[beginWord] = True
    length = 1
    while q:
        size = len(q)
        for i in range(size):
            currentWord = q.popleft()
            if currentWord == endWord:
                return length
            wordMatch(currentWord, visited, q)
        length += 1
    return 0


def main():
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    print("Output:", ladderLength(beginWord1, endWord1, wordList1))
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    print("Output:", ladderLength(beginWord2, endWord2, wordList2))


if __name__ == "__main__":
    main()


'''
Let N be dictionary size and L the common word length.
Time: O(N*L^2) expected: each word is enqueued once; its L positions try
26 letters, each requiring an O(L) string join/hash. Alphabet 26 is constant.
Space: O(N*L) for sets/maps/queued word strings, plus O(L) mutation buffer.
BFS levels count words in the shortest ladder; endWord must be in wordList.
'''
