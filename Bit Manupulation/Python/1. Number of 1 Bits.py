# Function to count the number of set bits in an integer `n`
def countSetBits(n):
    # Variable to store the count of set bits
    result = 0
    # Helper variable initialized to 1 (binary: 0001)
    helper = 1
    # Loop through all 32 bits (for 32-bit integers)
    for i in range(1, 33):
        # Check if the bit at the current position is set
        # Perform bitwise AND between `helper` and `n`
        if (helper & n) != 0:
            # Increment the result if the bit is set
            result += 1
        # Left shift `helper` by 1 to check the next bit in the next iteration
        helper = helper << 1
    # Return the total count of set bits
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
