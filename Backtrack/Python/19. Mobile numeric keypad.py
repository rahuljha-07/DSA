import sys


# Function to check if a move is valid (i.e., within bounds of the keypad matrix)
def isValid(row, col):
    # Skip * and #
    return 0 <= row < 4 and 0 <= col < 3 and not (row == 3 and col in (0, 2))


# Recursive function to generate all possible sequences
def generateSequences(row, col, n, current, keypad, result):
    # Base case: If length of the current sequence is n, add it to result
    if n == 0:
        result.append("".join(current))
        return
    moves = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(5):
        newRow = row + moves[i][0]
        newCol = col + moves[i][1]
        # Ensure the move is valid
        if isValid(newRow, newCol):
            # Append the new digit to the sequence
            current.append(chr(ord('0') + keypad[newRow][newCol]))
            # Recurse for the next digit
            generateSequences(newRow, newCol, n - 1, current, keypad, result)
            current.pop()


def main():
    keypad = [[1,2,3], [4,5,6], [7,8,9], [10,0,11]]
    print("Enter the length of the sequence (n): ", end="")
    n = int(sys.stdin.read())
    if n <= 0:
        raise ValueError("Sequence length must be positive")
    result = []
    for row in range(4):
        for col in range(3):
            if keypad[row][col] not in (10, 11):
                current = [chr(ord('0') + keypad[row][col])]
                generateSequences(row, col, n - 1, current, keypad, result)
    print(f"Total number of sequences of length {n}: {len(result)}")
    for seq in result:
        print(seq)


if __name__ == "__main__":
    main()


'''
Let n>=1 be sequence length and P the number of generated sequences.
Time: O(10*5^(n-1) + P*n) upper bound: ten starting digits, at most five
stay/adjacent moves per later digit, and O(n) joining per completed string.
Invalid keypad positions prune many branches.
Space: O(n) auxiliary mutable current sequence/recursion, plus O(P*n)
output strings. This enumerates sequences rather than using counting DP.
'''
