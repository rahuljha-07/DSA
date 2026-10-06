# Function to find the lexicographically smallest string
def chooseAndSwap(str):
    # Set to store remaining characters
    remainingChars = set()
    n = len(str)
    # Step 1: Add all characters of the string to the set
    for i in range(n):
        remainingChars.add(str[i])
    str = list(str)
    # Step 2: Iterate through the string
    for i in range(n):
        remainingChars.discard(str[i])
        # If no remaining characters, break
        if not remainingChars:
            break
        # Find the smallest character in the remaining set
        smallestChar = min(remainingChars)
        # Check if swapping the current character with the smallest character is beneficial
        if smallestChar < str[i]:
            currentChar = str[i]
            # Step 3: Perform the swap operation
            for j in range(n):
                if str[j] == currentChar:
                    str[j] = smallestChar
                elif str[j] == smallestChar:
                    str[j] = currentChar
            # Break after the first beneficial swap
            break
    # Return the resulting string
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
