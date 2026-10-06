# Recursive function to form sentences from the word lists
def solve(row, ans, matrix):
    # Base case: If all rows are processed, print the sentence
    if row == len(matrix):
        print(ans)
        return

    # Dynamically get size for the current row
    colSize = len(matrix[row])

    # Loop through each word in the current row
    for i in range(colSize):
        word = matrix[row][i]
        # Add space only if ans is not empty
        solve(row + 1, ans + ("" if ans == "" else " ") + word, matrix)


# Wrapper function to initiate the recursive process
def generateSentences(matrix):
    if len(matrix) == 0:
        return
    solve(0, "", matrix)


# with backtrack because we passed ans as reference
def solveBacktrack(row, col, ans, matrix):
    # Base case: If we've processed all rows (word lists), print the sentence
    if row == len(matrix):
        # Print the formed sentence
        print(ans[0])
        return

    for i in range(col):
        # Select the word from the current row
        word = matrix[row][i]

        oldAns = ans[0]
        ans[0] += ("" if ans[0] == "" else " ") + word
        # Recur to process the next row
        solveBacktrack(row + 1, col, ans, matrix)
        ans[0] = oldAns


matrix = [
    ["you", "we"],
    ["have", "are"],
    ["sleep", "eat", "drink"]
]

generateSentences(matrix)


'''
Time Complexity: O(k^r * r), where r is number of rows and k is average words per row.

Reason:
For every row, the recursion chooses one word.
If each row has about k choices and there are r rows,
the number of generated sentences is k^r.

Building or printing each sentence involves up to r words,
so the total work is O(k^r * r).

Space Complexity: O(r), excluding output.

Reason:
The recursion depth is equal to the number of rows.
Printed/generated sentences are output, so they are not counted
as auxiliary space.
'''
