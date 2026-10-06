def isPowerOfTwoUsingBitwise(n):
    # Negative numbers and 0 are not powers of 2
    if n <= 0:
        return False
    # Check if n has only one set bit
    return (n & (n - 1)) == 0


def isPowerOfTwoUsingCount(n):
    if n <= 0:
        return False
    count = 0
    while n > 0:
        # Check if the least significant bit is set
        count += n & 1
        # Right shift to process the next bit
        n = n >> 1
    # A number is a power of 2 if it has exactly 1 set bit
    return count == 1


def main():
    n = 8
    print("Using n & (n - 1):")
    print(f"Is {n} a power of 2? {str(isPowerOfTwoUsingBitwise(n)).lower()}")
    print("Using Counting Set Bits:")
    print(f"Is {n} a power of 2? {str(isPowerOfTwoUsingCount(n)).lower()}")


if __name__ == "__main__":
    main()


'''
Time: bitwise method O(1), since it performs one subtraction and AND;
counting method O(log(n+1)), since it removes one bit per right shift.
Space: O(1) scalar storage for both, assuming fixed-width-sized integers.
For arbitrary Python big integers, bitwise operations scan their stored
digits; the bitwise method takes O(b) time/space for b-bit n, while
repeated shifts can take O(b^2) time and O(b) live storage.
'''
