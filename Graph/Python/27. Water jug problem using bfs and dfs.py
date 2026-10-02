from collections import deque
from math import gcd


def waterJugBFS(m, n, d):
    if d == 0:
        return 0
    if d > max(m, n) or gcd(m, n) == 0 or d % gcd(m, n) != 0:
        return -1
    visited = set()
    q = deque([((0, 0), 0)])
    while q:
        current, steps = q.popleft()
        jug1, jug2 = current
        if jug1 == d or jug2 == d:
            return steps
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        q.append(((m, jug2), steps + 1))
        q.append(((jug1, n), steps + 1))
        q.append(((0, jug2), steps + 1))
        q.append(((jug1, 0), steps + 1))
        q.append(((min(jug1 + jug2, m), max(jug1 + jug2 - m, 0)), steps + 1))
        q.append(((max(jug1 + jug2 - n, 0), min(jug1 + jug2, n)), steps + 1))
    return -1


def dfsHelper(jug1, jug2, m, n, d, visited, steps):
    if jug1 == d or jug2 == d:
        return True
    if (jug1, jug2) in visited:
        return False
    visited.add((jug1, jug2))
    steps[0] += 1
    if dfsHelper(m, jug2, m, n, d, visited, steps):
        return True
    if dfsHelper(jug1, n, m, n, d, visited, steps):
        return True
    if dfsHelper(0, jug2, m, n, d, visited, steps):
        return True
    if dfsHelper(jug1, 0, m, n, d, visited, steps):
        return True
    if dfsHelper(min(jug1 + jug2, m), max(jug1 + jug2 - m, 0), m, n, d, visited, steps):
        return True
    if dfsHelper(max(jug1 + jug2 - n, 0), min(jug1 + jug2, n), m, n, d, visited, steps):
        return True
    steps[0] -= 1
    return False


def waterJugDFS(m, n, d):
    if d == 0:
        return 0
    if d > max(m, n) or gcd(m, n) == 0 or d % gcd(m, n) != 0:
        return -1
    visited = set()
    steps = [0]
    if dfsHelper(0, 0, m, n, d, visited, steps):
        return steps[0]
    return -1


def main():
    m = 3
    n = 5
    d = 4
    print("Using BFS:", waterJugBFS(m, n, d), "steps")
    print("Using DFS:", waterJugDFS(m, n, d), "steps")


if __name__ == "__main__":
    main()


'''
Let S <= (m+1)*(n+1) be reachable integer water-volume states.
Time: O(S) expected: each state is expanded once, producing six possible
fill/empty/pour transitions; hash-set checks average O(1).
Space: O(S) auxiliary visited and queue/DFS stack; duplicate queued states
add at most a constant factor. The gcd feasibility test is logarithmic.
BFS returns the minimum number of operations; the retained DFS returns
a successful search-path length, not necessarily the minimum.
Capacities/target are nonnegative integers; zero target needs zero moves.
'''
