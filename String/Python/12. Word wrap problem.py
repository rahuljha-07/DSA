# Global memoization table
dp = []


# Helper function to calculate minimum cost
def findMinCost(wordIndex, currentLineWidth, wordLengths, maxLineWidth):
    # Base case: all words processed
    if wordIndex == len(wordLengths):
        return 0

    # Return already computed result
    if dp[wordIndex][currentLineWidth] != -1:
        return dp[wordIndex][currentLineWidth]

    costIfSameLine = float('inf')

    # Width if current word is added to same line
    newLineWidth = currentLineWidth + 1 + wordLengths[wordIndex]

    # Continue on same line if possible
    if newLineWidth <= maxLineWidth:
        costIfSameLine = findMinCost(
            wordIndex + 1,
            newLineWidth,
            wordLengths,
            maxLineWidth
        )

    # Start a new line and add cost of unused spaces
    costIfNewLine = (
        findMinCost(
            wordIndex + 1,
            wordLengths[wordIndex],
            wordLengths,
            maxLineWidth
        )
        +
        (maxLineWidth - currentLineWidth) *
        (maxLineWidth - currentLineWidth)
    )

    # Store minimum cost
    dp[wordIndex][currentLineWidth] = min(
        costIfSameLine,
        costIfNewLine
    )

    return dp[wordIndex][currentLineWidth]


# Main function
def solveWordWrap(wordLengths, maxLineWidth):
    global dp

    totalWords = len(wordLengths)

    # Initialize memoization table
    dp = [
        [-1 for _ in range(maxLineWidth + 1)]
        for _ in range(totalWords + 1)
    ]

    return findMinCost(
        1,
        wordLengths[0],
        wordLengths,
        maxLineWidth
    )


# Input
totalWords = int(input())

wordLengths = list(map(int, input().split()))

maxLineWidth = int(input())

print(solveWordWrap(wordLengths, maxLineWidth))


'''
Time Complexity:
O(n * W)

Reason:

The state is defined by:

wordIndex
currentLineWidth

There can be at most:

n * W

different states.

Because of memoization, each state is calculated only once.

For each state, we perform only constant-time work.

Therefore:

O(n * W)

where:
n = number of words
W = maxLineWidth


Space Complexity:
O(n * W)

Reason:

The memoization table dp has dimensions:

(n + 1) x (W + 1)

Therefore:

O(n * W)

There is also recursion stack space of O(n),
but O(n * W) dominates it.
'''