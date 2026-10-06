def Anagrams(inputStrings):
    # Map to store sorted strings as keys and their corresponding anagrams as values
    anagramMap = {}

    # Iterate through each string in the input list
    for i in range(len(inputStrings)):
        # Get the current string
        currentString = inputStrings[i]
        currentString = "".join(sorted(currentString))
        if currentString not in anagramMap:
            anagramMap[currentString] = []
        # Add original string to the corresponding anagram group
        anagramMap[currentString].append(inputStrings[i])

    anagramGroups = []

    # Iterate through the map and populate the output list with anagram groups
    for pair in sorted(anagramMap):
        anagrams = anagramMap[pair]
        anagramGroups.append([])
        for j in range(len(anagrams)):
            # Add each anagram to the output
            anagramGroups[-1].append(anagrams[j])

    # Return the final list of anagram groups
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
