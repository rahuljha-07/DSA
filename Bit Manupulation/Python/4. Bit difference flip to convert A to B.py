# Function to count the number of bits to flip
def countBitsFlip(A, B):
    # XOR A and B
    xorResult = A ^ B
    # Initialize the count of bits to flip
    count = 0
    # Count the number of set bits in xorResult
    while xorResult > 0:
        # Check if the least significant bit is set
        count += xorResult & 1
        # Right shift the result by 1
        xorResult = xorResult >> 1
    # Return the total count
    return count


def main():
    A = 10
    B = 20
    print(f"Number of bits to flip to convert {A} to {B}: {countBitsFlip(A, B)}")


if __name__ == "__main__":
    main()


'''
For nonnegative A and B, let b be the bit length of A XOR B.
Time: O(b): each iteration counts the low bit and shifts away one bit.
Space: O(1) scalar variables under the source's fixed-width model.
For 32-bit inputs b<=32, so time is also O(1). As in the source, a
negative XOR is not processed; this function assumes nonnegative inputs.
'''
