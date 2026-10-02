def Anagrams(inputStrings):
    anagramMap = {}

    for i in range(len(inputStrings)):
        currentString = inputStrings[i]
        currentString = "".join(sorted(currentString))
        if currentString not in anagramMap:
            anagramMap[currentString] = []
        anagramMap[currentString].append(inputStrings[i])

    anagramGroups = []

    for pair in sorted(anagramMap):
        anagrams = anagramMap[pair]
        anagramGroups.append([])
        for j in range(len(anagrams)):
            anagramGroups[-1].append(anagrams[j])

    return anagramGroups


inputStrings = ["act", "god", "cat", "dog", "tac"]
print(Anagrams(inputStrings))


'''
Time Complexity: O(n * m log m), where n is number of strings and m is average string length.

Reason:
For each of the n strings, we sort its characters.
Sorting one string of length m costs O(m log m).
Then we use the sorted string as a dictionary key to group anagrams.

Space Complexity: O(n * m)

Reason:
The map stores all strings inside anagram groups.
The sorted keys also store characters from the input strings.
'''
