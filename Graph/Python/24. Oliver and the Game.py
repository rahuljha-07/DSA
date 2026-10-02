import sys


inTime = []
outTime = []
timer = 1


def resize(n):
    inTime[:] = [0] * (n + 1)
    outTime[:] = [0] * (n + 1)


def dfs(src, par, g):
    global timer
    inTime[src] = timer
    timer += 1
    for x in g[src]:
        if x != par:
            dfs(x, src, g)
    outTime[src] = timer
    timer += 1


def check(x, y):
    return inTime[x] <= inTime[y] and outTime[x] >= outTime[y]


def main():
    global timer
    tokens = iter(sys.stdin.read().split())
    n = int(next(tokens))
    timer = 1
    resize(n)
    g = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        x = int(next(tokens))
        y = int(next(tokens))
        g[x].append(y)
        g[y].append(x)
    dfs(1, 0, g)
    q = int(next(tokens))
    for i in range(q):
        type = int(next(tokens))
        x = int(next(tokens))
        y = int(next(tokens))
        if not check(x, y) and not check(y, x):
            print("NO")
            continue
        if type == 0:
            print("YES" if check(y, x) else "NO")
        else:
            print("YES" if check(x, y) else "NO")


if __name__ == "__main__":
    main()


'''
Let n be nodes in the tree and q queries.
Time: O(n + q): one DFS records entry/exit times; each ancestry check
uses two comparisons, so each query is O(1).
Space: O(n) auxiliary times and DFS depth, plus O(n) supplied adjacency.
The source's type/x/y query orientation is retained. check(x,y) means
x is an ancestor of y, including x==y; input must be a connected tree.
'''
