import sys


def countBBT(h):
    if h == 0:
        return 1
    if h == 1:
        return 1
    samelevel = countBBT(h - 1)
    difflevel = countBBT(h - 2)
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
