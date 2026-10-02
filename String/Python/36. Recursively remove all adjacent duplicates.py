def removeAdjacentDuplicates(S):
    if len(S) == 0 or len(S) == 1:
        return S

    result = ""
    hasAdjacentDuplicates = False

    i = 0
    while i < len(S):
        if i < len(S) - 1 and S[i] == S[i + 1]:
            hasAdjacentDuplicates = True
            while i < len(S) - 1 and S[i] == S[i + 1]:
                i += 1
        else:
            result += S[i]
        i += 1

    return removeAdjacentDuplicates(result) if hasAdjacentDuplicates else result


input1 = "geeksforgeek"
input2 = "abccbccba"

print("Input:", input1, "-> Output:", removeAdjacentDuplicates(input1))
print("Input:", input2, "-> Output:", removeAdjacentDuplicates(input2))


'''
Time Complexity: O(n^2) in the worst case.

Reason:
Each recursive call scans the current string once.
In the worst case, only a small part is removed per call,
so there can be multiple scans of strings close to length n.
That makes the worst-case work O(n^2).

Space Complexity: O(n)

Reason:
Each call builds a temporary result string.
The recursion stack can also grow with the number of passes.
'''
