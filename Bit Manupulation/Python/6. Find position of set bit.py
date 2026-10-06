def findPositionOfSetBit(N):
    # Step 1: Check if N is a power of 2.
    # A power of 2 has only one set bit.
    # Use the condition (N & (N - 1)) == 0 to validate.
    if N <= 0 or (N & (N - 1)) != 0:
        # Return -1 if N is not a power of 2
        return -1
    # Step 2: Find the position of the set bit.
    # Initialize position to 1 (counting starts from 1).
    # Right shift N until the least significant bit (LSB) is 1.
    position = 1
    # Check if LSB is 0
    while (N & 1) == 0:
        # Right shift N by 1
        N = N >> 1
        # Increment position counter
        position += 1
    # Return the position of the set bit
    return position


def main():
    for N in (2, 5, 16):
        print(f"Position of set bit in {N}: {findPositionOfSetBit(N)}")


if __name__ == "__main__":
    main()


'''
Time: O(log(N+1)) for a valid positive power of two: shift once for
every zero below its only set bit. Invalid inputs return after one check.
Space: O(1) scalar variables under fixed-width integer costs.
With arbitrary b-bit Python integers, repeated shifts have O(b^2)
worst-case bit work and O(b) live integer storage.
'''
