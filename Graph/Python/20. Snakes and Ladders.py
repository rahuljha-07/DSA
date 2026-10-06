from collections import deque


def snakesAndLadders(board):
    n = len(board)
    if n == 0:
        return -1
    if n == 1:
        return 0
    # Ladder map
    lad = {}
    # Snake map
    sna = {}
    # Create the snake and ladder maps
    # Square number
    sq = 1
    leftToRight = True
    for i in range(n - 1, -1, -1):
        columns = range(n) if leftToRight else range(n - 1, -1, -1)
        for j in columns:
            if board[i][j] != -1:
                # Ladder
                if board[i][j] > sq:
                    lad[sq] = board[i][j]
                else:
                    sna[sq] = board[i][j]
            sq += 1
        leftToRight = not leftToRight
    # BFS to calculate minimum moves
    moves = 0
    # Begin BFS at square 1 with zero moves made.
    q = deque([1])
    found = False
    # Visited array
    vis = [False] * (n * n + 1)
    vis[1] = True
    while q and not found:
        sz = len(q)
        while sz:
            t = q.popleft()
            for die in range(1, 7):
                next = t + die
                if next > n * n:
                    continue
                destination = lad.get(next, sna.get(next, next))
                if destination == n * n:
                    found = True
                if not vis[destination]:
                    vis[destination] = True
                    q.append(destination)
            sz -= 1
        moves += 1
    return moves if found else -1


def main():
    board = [[-1] * 6 for _ in range(6)]
    board[3][1] = 35
    board[3][4] = 13
    board[5][1] = 15
    print(snakesAndLadders(board))


if __name__ == "__main__":
    main()


'''
Let n be board width and S=n^2 the number of squares.
Time: O(S) expected: scan board once, then BFS each destination once with
six constant die outcomes. Dictionaries replace C++ ordered maps.
Space: O(S) auxiliary maps, visited, and queue.
Only one snake/ladder jump occurs per move. Winning is checked AFTER
that jump, so a snake at the last square cannot falsely finish the game.
'''
