def solve(row, ans, matrix):
    if row == len(matrix):
        print(ans)
        return

    colSize = len(matrix[row])

    for i in range(colSize):
        word = matrix[row][i]
        solve(row + 1, ans + ("" if ans == "" else " ") + word, matrix)


def generateSentences(matrix):
    if len(matrix) == 0:
        return
    solve(0, "", matrix)


def solveBacktrack(row, col, ans, matrix):
    if row == len(matrix):
        print(ans[0])
        return

    for i in range(col):
        word = matrix[row][i]

        oldAns = ans[0]
        ans[0] += ("" if ans[0] == "" else " ") + word
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
