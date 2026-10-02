def countSetBits(n):
    result = 0
    helper = 1
    for i in range(1, 33):
        if (helper & n) != 0:
            result += 1
        helper = helper << 1
    return result


def main():
    n = 11
    print(f"Number of set bits in {n} is: {countSetBits(n)}")


if __name__ == "__main__":
    main()


'''
Time: O(1): the loop checks exactly 32 positions, regardless of n.
Space: O(1): only result, helper, and the loop index are stored.
Like the source, this counts the low 32 bits, including the two's-complement
representation of negative 32-bit integers.
'''
