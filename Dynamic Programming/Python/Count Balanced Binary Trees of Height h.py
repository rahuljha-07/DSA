import sys


# Recursive function to count the number of balanced binary trees of height h
def countBBT(h):
    # Base cases:
    # An empty tree is balanced
    if h == 0:
        return 1
    # A single-node tree is balanced
    if h == 1:
        return 1
    # Recursive calls:
    # Count of trees of height h-1
    samelevel = countBBT(h - 1)
    # Count of trees of height h-2
    difflevel = countBBT(h - 2)
    # Total number of trees for height h:
    # - Case 1: Both subtrees are of height h-1 => samelevel * samelevel
    # - Case 2: One subtree of height h-1 and the other of height h-2 => 2 * samelevel *
    # difflevel
    return samelevel * samelevel + 2 * samelevel * difflevel


def main():
    h = int(sys.stdin.read())
    print(countBBT(h))


if __name__ == "__main__":
    main()


'''
Let h>=0 be tree height.
Time: O(phi^h) recursive calls, phi=(1+sqrt(5))/2: both h-1 and h-2
are recomputed without memoization, giving the Fibonacci call recurrence.
This counts arithmetic operations only, not big-integer multiplication.
Space: O(h) recursive frames under unit-size values. Actual counts grow
very large (O(2^h) bits), so Python integer storage/multiplication dominate
for large h. The source's unmemoized recursion is deliberately retained.
'''
