def dfs(node, adj, visited, size):
    visited[node] = True
    size[0] += 1
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor, adj, visited, size)


def journeyToMoon(n, astronaut):
    adj = [[] for _ in range(n)]
    for pair in astronaut:
        adj[pair[0]].append(pair[1])
        adj[pair[1]].append(pair[0])
    visited = [False] * n
    sizes = []
    for i in range(n):
        if not visited[i]:
            size = [0]
            dfs(i, adj, visited, size)
            sizes.append(size[0])
    totalPairs = n * (n - 1) // 2
    invalidPairs = 0
    for size in sizes:
        invalidPairs += size * (size - 1) // 2
    return totalPairs - invalidPairs


def main():
    n = 5
    astronaut = [[0, 1], [2, 3], [0, 4]]
    print("Valid pairs:", journeyToMoon(n, astronaut))
    n = 4
    astronaut = [[0, 2]]
    print("Valid pairs:", journeyToMoon(n, astronaut))


if __name__ == "__main__":
    main()


'''
Let n be astronauts and E known same-country pairs.
Time: O(n + E): build adjacency, visit each component once, then subtract
one constant-time pair count per component.
Space: O(n + E) auxiliary adjacency, visited, component sizes, and recursion.
Integer division preserves exact counts rather than using floating-point math.
'''
