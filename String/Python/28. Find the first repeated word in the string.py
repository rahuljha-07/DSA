def findSecondMostFrequentString(arr, n):
    # Map to store the frequency of each string
    frequencyMap = {}

    # Count the frequency of each string in the array
    for i in range(n):
        frequencyMap[arr[i]] = frequencyMap.get(arr[i], 0) + 1

    maxFreq1 = -10**9
    maxFreq2 = -10**9

    # Variables to store the corresponding strings
    # String with the first maximum frequency
    resultMax1 = ""
    # String with the second maximum frequency
    resultMax2 = ""

    # Iterate through the frequency map to find the first and second most frequent strings
    for entry in frequencyMap:
        # Current frequency of the string
        currentFreq = frequencyMap[entry]

        # Check if current frequency is greater than the first maximum
        if currentFreq > maxFreq1:
            # Update second maximum to first maximum
            maxFreq2 = maxFreq1
            # Update first maximum
            maxFreq1 = currentFreq

            # Update the second result to the first result
            resultMax2 = resultMax1
            # Update the first result to the current string
            resultMax1 = entry
        # Check if current frequency is the second maximum and not equal to the first
        # maximum
        elif currentFreq > maxFreq2 and currentFreq != maxFreq1:
            # Update second maximum frequency
            maxFreq2 = currentFreq
            # Update second result to the current string
            resultMax2 = entry

    return resultMax2


arr = ["aaa", "bbb", "ccc", "bbb", "aaa", "aaa"]
n = len(arr)
secondMostFrequent = findSecondMostFrequentString(arr, n)
print("The second most repeated string is:", secondMostFrequent)


'''
Time Complexity: O(n), where n is the number of strings.

Reason:
The first loop counts frequency of every string once.
The second loop scans the frequency map once to find the top two
different frequencies.

Together, the work is linear in the number of strings.

Space Complexity: O(n)

Reason:
In the worst case, every string is different, so the frequency map
stores n entries.
'''
