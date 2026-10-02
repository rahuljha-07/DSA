vector<vector<string>> Anagrams(vector<string>& inputStrings) {
    // Map to store sorted strings as keys and their corresponding anagrams as values
    map<string, vector<string>> anagramMap;

    // Iterate through each string in the input vector
    for (auto i = 0; i < inputStrings.size(); i++) {
        string currentString = inputStrings[i];  // Get the current string
        sort(currentString.begin(), currentString.end());  // Sort the string to identify anagrams
        anagramMap[currentString].push_back(inputStrings[i]);  // Add original string to the corresponding anagram group
    }

    // Vector to hold the final list of anagram groups
    vector<vector<string>> anagramGroups(anagramMap.size());
    auto index = 0;  // Index for the final output vector

    // Iterate through the map and populate the output vector with anagram groups
    for (auto& pair : anagramMap) {
        vector<string> anagrams = pair.second;  // Get the list of anagrams
        for (auto j = 0; j < anagrams.size(); j++) {
            anagramGroups[index].push_back(anagrams[j]);  // Add each anagram to the output
        }
        index++;  // Move to the next index for the output
    }

    return anagramGroups;  // Return the final list of anagram groups
}