from collections import deque


v = []


def dfs(i, j, s, m, n):
    if i < 0 or j < 0 or i >= n or j >= n or m[i][j] == 0:
        return
    if i == n - 1 and j == n - 1:
        v.append(s)
        return
    m[i][j] = 0
    dfs(i - 1, j, s + 'U', m, n)
    dfs(i + 1, j, s + 'D', m, n)
    dfs(i, j - 1, s + 'L', m, n)
    dfs(i, j + 1, s + 'R', m, n)
    m[i][j] = 1


def findPath(m, n):
    v.clear()
    if n == 0 or m[0][0] == 0 or m[n - 1][n - 1] == 0:
        return list(v)
    s = ""
    dfs(0, 0, s, m, n)
    v.sort()
    return list(v)


def findPathBFS(m, n):
    paths = []
    if n == 0 or m[0][0] == 0 or m[n - 1][n - 1] == 0:
        return paths
    directions = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]
    q = deque([((0, 0), "")])
    m[0][0] = 0
    while q:
        (i, j), path = q.popleft()
        if i == n - 1 and j == n - 1:
            paths.append(path)
            continue
        for di, dj, dir in directions:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n and m[ni][nj] == 1:
                q.append(((ni, nj), path + dir))
                m[ni][nj] = 0
    paths.sort()
    return paths


'''
Let A=n^2 be cells and P the number of DFS result paths, length at most A.
DFS time: O(A*4^A + P*A*log(P+1)) conservative bound: explore simple-path
branches, copy path strings, then sort P strings with up to A comparisons.
DFS space: O(A^2) auxiliary retained path prefixes/stack, plus O(P*A) output.
DFS restores the maze after backtracking.
BFS time: O(A^2) worst case because A enqueues copy paths up to length A.
BFS space: O(A^2) queued strings worst-case bound. Source behavior retained:
global marking means at most ONE shortest path, not all paths, and it
modifies m permanently. The two methods therefore are not equivalent.
'''
