def minFlipsToAlternating(s):
    countFlipsToPattern1 = 0
    countFlipsToPattern2 = 0

    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == '1':
                countFlipsToPattern1 += 1
            else:
                countFlipsToPattern2 += 1
        else:
            if s[i] == '0':
                countFlipsToPattern1 += 1
            else:
                countFlipsToPattern2 += 1

    return min(countFlipsToPattern1, countFlipsToPattern2)


binaryString = "001"
result = minFlipsToAlternating(binaryString)
print("Minimum number of flips:", result)


'''
Time Complexity: O(n), where n is the string length.

Reason:
The string is scanned once.
At each index, we compare the current character with the two possible
alternating patterns and update counters.

Space Complexity: O(1)

Reason:
Only two counters and loop variables are used.
No extra structure depends on n.
'''
