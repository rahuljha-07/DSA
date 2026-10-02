import sys


def copySetBitsInRange(a, b, left, right):
    mask = (1 << (right - left + 1)) - 1
    mask = mask << (left - 1)
    mask = mask & a
    b = b | mask
    return b


def main():
    print("Enter values for a, b, left, and right:")
    a, b, left, right = map(int, sys.stdin.read().split())
    result = copySetBitsInRange(a, b, left, right)
    print("Updated value of b:", result)


if __name__ == "__main__":
    main()


'''
Time: O(1) for fixed-width integers: build, align, AND, and OR one mask;
there is no loop over the selected positions. Positions are 1-based.
Space: O(1) fixed-width scalar storage.
For arbitrary Python big integers, time and live space are O(B), where B
covers operand bit lengths and right. Assumes 1<=left<=right.
'''
