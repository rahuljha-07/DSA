def minimumNumberOfSwaps(str):
    # Variable to store the number of swaps needed
    ans = 0
    # To count the open brackets
    bracketCount = 0

    for i in range(len(str)):
        if str[i] == '[':
            # Increment for an open bracket
            bracketCount += 1
        else:
            # Decrement for a close bracket
            bracketCount -= 1
            # If there are more close brackets
            if bracketCount < 0:
                ans = ans - bracketCount

    # Return the total number of swaps needed
    return ans


str = "][]["
print(minimumNumberOfSwaps(str))


'''
Time Complexity: O(n), where n is the string length.

Reason:
The string is traversed once.
Each character updates bracketCount and sometimes ans in constant time.

Space Complexity: O(1)

Reason:
Only integer variables are used.
No stack, list, or map grows with the input.
'''
