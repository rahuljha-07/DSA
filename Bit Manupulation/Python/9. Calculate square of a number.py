import sys


def square(n):
    # Initialize the result
    result = 0
    n = abs(n)
    # Make the number positive (to handle negative inputs)
    x = n
    # Bit position
    i = 0
    while x > 0:
        # Check if the ith bit of x is set.
        # If it is, add (n << i) to the result.
        # - n << i is equivalent to n multiplied by 2^i.
        if x & 1:
            # Add the shifted value to the result
            result += n << i
        # Move to the next bit by right-shifting x
        x = x >> 1
        # Increment the bit position
        i += 1
    return result


def main():
    print("Enter a number: ", end="")
    n = int(sys.stdin.read())
    print(f"Square of {n} is: {square(n)}")


if __name__ == "__main__":
    main()


'''
Time: O(log(|n|+1)) iterations: each iteration consumes one bit of |n|
and, when set, adds its shifted contribution. Zero takes constant time.
Space: O(1) scalar storage under fixed-width arithmetic.
For b-bit arbitrary Python input, shifts/additions can cost O(b) each,
giving O(b^2) bit work and O(b) live storage, including the square.
The source shifted signed n despite making only x positive; using |n|
for both fixes negative inputs without changing the bit-addition approach.
'''
