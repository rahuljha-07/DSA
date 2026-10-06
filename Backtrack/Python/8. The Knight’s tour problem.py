import sys


def displayBoard(chess):
    # Iterate over rows
    for i in range(len(chess)):
        # Iterate over columns
        # Print each cell
        for j in range(len(chess[i])):
            print(chess[i][j], end=" ")
        print()
    print()


# Recursive function to find and print all possible knight's tours
def printKnightsTour(chess, row, col, move):
    if (row < 0 or col < 0 or row >= len(chess) or col >= len(chess)
            or chess[row][col] != 0):
        return
    # If all cells are visited, print the chessboard
    if move == len(chess) * len(chess):
        # Mark the last move
        chess[row][col] = move
        # Display the complete tour
        displayBoard(chess)
        # Backtrack
        chess[row][col] = 0
        return
    # Mark the current cell with the current move number
    chess[row][col] = move
    printKnightsTour(chess, row - 2, col + 1, move + 1)
    # Recursively try all 8 possible knight moves
    # Move 1
    printKnightsTour(chess, row - 1, col + 2, move + 1)
    # Move 2
    # Move 3
    printKnightsTour(chess, row + 1, col + 2, move + 1)
    # Move 4
    printKnightsTour(chess, row + 2, col + 1, move + 1)
    # Move 5
    # Move 6
    printKnightsTour(chess, row + 2, col - 1, move + 1)
    # Move 7
    printKnightsTour(chess, row + 1, col - 2, move + 1)
    # Move 8
    printKnightsTour(chess, row - 1, col - 2, move + 1)
    printKnightsTour(chess, row - 2, col - 1, move + 1)
    # Backtrack: Unmark the current cell
    chess[row][col] = 0


def main():
    tokens = iter(sys.stdin.read().split())
    print("Enter the size of the chessboard (n): ", end="")
    n = int(next(tokens))
    print("Enter the starting row: ", end="")
    startRow = int(next(tokens))
    print("Enter the starting column: ", end="")
    startCol = int(next(tokens))
    chess = [[0] * n for _ in range(n)]
    printKnightsTour(chess, startRow, startCol, 1)


if __name__ == "__main__":
    main()


'''
Let A=n^2 be board cells and T the printed complete tours.
Time: O(8^A + T*A) conservative upper bound: explore at most eight moves
per step to depth A; printing a complete board costs O(A).
Space: O(A) auxiliary recursive depth plus the O(A) supplied board.
No tours are stored; the board is marked/unmarked in place and restored.
This enumerates tours with the source's fixed move order, without heuristics.
'''
