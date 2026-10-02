def comp(a, b):
    return a[1] < b[1]


def maxChainLen(v, n):
    if n == 0:
        return 0
    v.sort(key=lambda a: a[1])
    count = 1
    lastEnd = v[0][1]
    for i in range(1, n):
        if v[i][0] > lastEnd:
            count += 1
            lastEnd = v[i][1]
    return count


def main():
    pairs = [(1, 2), (2, 3), (3, 4), (5, 6), (4, 7)]
    n = len(pairs)
    print("Maximum chain length:", maxChainLen(pairs, n))


if __name__ == "__main__":
    main()


'''
Let n=len(v) be pairs, each with first<second.
Time: O(n log(n+1)): sort by ending value, then scan once to accept
pairs whose starts are strictly after the last chosen end.
Space: O(n) auxiliary worst case for Python's sorting/key workspace;
the greedy scan itself needs O(1). v is reordered in place.
This preserves the source's greedy method despite being in the DP folder.
'''
