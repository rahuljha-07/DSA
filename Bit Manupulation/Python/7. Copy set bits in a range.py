import sys


def copySetBitsInRange(a, b, left, right):
    # Step 1: Create a mask for the range [left, right]
    # Create a mask with '1' in the range width
    mask = (1 << (right - left + 1)) - 1
    # Shift mask to align with the range
    mask = mask << (left - 1)
    # Extract the bits from `a` in the range
    mask = mask & a
    # Step 2: Copy the extracted bits to `b`
    b = b | mask
    # Return the updated `b`
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
