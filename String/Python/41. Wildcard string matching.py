memo = []


# Helper function to perform recursive pattern matching with wildcards
def matchPatternUtil(patternIdx, strIdx, patternLen, strLen, pattern, str):
    if patternIdx == patternLen and strIdx == strLen:
        return True
    elif strIdx == strLen:
        for k in range(patternIdx, patternLen):
            if pattern[k] != '*':
                return False
        return True
    elif patternIdx == patternLen:
        return False
    elif memo[patternIdx][strIdx] != -1:
        return memo[patternIdx][strIdx]

    result = False

    if pattern[patternIdx] == str[strIdx]:
        result = matchPatternUtil(patternIdx + 1, strIdx + 1, patternLen, strLen, pattern, str)
    elif pattern[patternIdx] == '?':
        result = matchPatternUtil(patternIdx + 1, strIdx + 1, patternLen, strLen, pattern, str)
    elif pattern[patternIdx] == '*':
        result = (matchPatternUtil(patternIdx + 1, strIdx, patternLen, strLen, pattern, str) or
                  matchPatternUtil(patternIdx, strIdx + 1, patternLen, strLen, pattern, str))
    else:
        result = False

    memo[patternIdx][strIdx] = result
    return memo[patternIdx][strIdx]


def isPatternMatch(pattern, str):
    global memo
    patternLen = len(pattern)
    strLen = len(str)
    # Resize and initialize memo table
    memo = [[-1 for j in range(strLen + 1)] for i in range(patternLen + 1)]
    return matchPatternUtil(0, 0, patternLen, strLen, pattern, str)


pattern = "ba*a?"
str = "baaabab"
print(isPatternMatch(pattern, str))


'''
Time Complexity: O(n * m), where n is pattern length and m is string length.

Reason:
Each recursive state is defined by patternIdx and strIdx.
There are n possible pattern indexes and m possible string indexes,
so there are O(n * m) states.

Memoization makes sure each state is solved once.
Each state does constant work except for recursive calls.

Space Complexity: O(n * m)

Reason:
The memo table stores one value for every pattern/string index pair.
The recursion stack can grow up to O(n + m), but the memo table dominates.
'''
