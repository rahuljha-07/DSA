INT_MAX = (1 << 31) - 1
INT_MIN = -(1 << 31)


def divide(a, b):
    if b == 0:
        return INT_MAX
    if a == INT_MIN and b == -1:
        return INT_MAX
    negative = (a < 0) ^ (b < 0)
    dividend = abs(a)
    divisor = abs(b)
    quotient = 0
    while dividend >= divisor:
        temp = divisor
        multiple = 1
        while (temp << 1) <= dividend:
            temp <<= 1
            multiple <<= 1
        dividend -= temp
        quotient += multiple
    if negative:
        quotient = -quotient
    if quotient > INT_MAX:
        return INT_MAX
    if quotient < INT_MIN:
        return INT_MIN
    return quotient


def main():
    for a, b in ((10, 3), (43, -8), (INT_MIN, 1)):
        print(f"Quotient of {a} / {b} = {divide(a, b)}")


if __name__ == "__main__":
    main()


'''
Let L be the bit length of the nonnegative quotient |a|//|b|, for b!=0.
Time: O((L+1)^2) under unit-cost arithmetic, NOT O(log|a|): the outer
loop removes the largest available divisor multiple; the inner doubling
scan restarts from divisor each time. For an all-ones quotient it performs
L+(L-1)+...+1 shifts. For 32-bit inputs L is bounded, hence O(1).
Space: O(1) scalar storage for fixed-width inputs.
With arbitrary B-bit Python operands, a conservative bound is O((L+1)^2*B)
bit work and O(B) live storage. Results truncate toward zero and clamp to
signed 32-bit bounds; division by zero returns INT_MAX as in the source.
'''
