def chooseAndSwap(str):
    remainingChars = set()
    n = len(str)
    for i in range(n):
        remainingChars.add(str[i])
    str = list(str)
    for i in range(n):
        remainingChars.discard(str[i])
        if not remainingChars:
            break
        smallestChar = min(remainingChars)
        if smallestChar < str[i]:
            currentChar = str[i]
            for j in range(n):
                if str[j] == currentChar:
                    str[j] = smallestChar
                elif str[j] == smallestChar:
                    str[j] = currentChar
            break
    return "".join(str)


def main():
    str = "ccad"
    print("Original string:", str)
    result = chooseAndSwap(str)
    print("Lexicographically smallest string:", result)
    str = "abba"
    print("Original string:", str)
    result = chooseAndSwap(str)
    print("Lexicographically smallest string:", result)


if __name__ == "__main__":
    main()


'''
Let n be characters and A distinct characters.
Time: O(n*A) worst-case bound: set membership/removal averages O(1),
but min(remainingChars) scans up to A entries per position. The eventual
global character swap is O(n). For fixed lowercase alphabet A<=26, O(n).
Space: O(n+A) auxiliary character list/set, plus O(n) output string.
The set need not be ordered because only its minimum is queried.
'''
