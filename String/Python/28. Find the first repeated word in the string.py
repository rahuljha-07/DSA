def findSecondMostFrequentString(arr, n):
    frequencyMap = {}

    for i in range(n):
        frequencyMap[arr[i]] = frequencyMap.get(arr[i], 0) + 1

    maxFreq1 = -10**9
    maxFreq2 = -10**9

    resultMax1 = ""
    resultMax2 = ""

    for entry in frequencyMap:
        currentFreq = frequencyMap[entry]

        if currentFreq > maxFreq1:
            maxFreq2 = maxFreq1
            maxFreq1 = currentFreq

            resultMax2 = resultMax1
            resultMax1 = entry
        elif currentFreq > maxFreq2 and currentFreq != maxFreq1:
            maxFreq2 = currentFreq
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
