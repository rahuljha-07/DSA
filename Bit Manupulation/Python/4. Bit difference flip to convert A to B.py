def countBitsFlip(A, B):
    xorResult = A ^ B
    count = 0
    while xorResult > 0:
        count += xorResult & 1
        xorResult = xorResult >> 1
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
