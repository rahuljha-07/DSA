import sys


def square(n):
    result = 0
    n = abs(n)
    x = n
    i = 0
    while x > 0:
        if x & 1:
            result += n << i
        x = x >> 1
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
