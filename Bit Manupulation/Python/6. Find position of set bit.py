def findPositionOfSetBit(N):
    if N <= 0 or (N & (N - 1)) != 0:
        return -1
    position = 1
    while (N & 1) == 0:
        N = N >> 1
        position += 1
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
