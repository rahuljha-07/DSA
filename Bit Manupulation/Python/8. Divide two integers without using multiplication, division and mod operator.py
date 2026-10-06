INT_MAX = (1 << 31) - 1
INT_MIN = -(1 << 31)


def divide(a, b):
    # Edge case: Division by 0
    # Division by 0 is undefined
    if b == 0:
        return INT_MAX
    if a == INT_MIN and b == -1:
        return INT_MAX
    # Determine the sign of the result
    # XOR to check if signs are different
    negative = (a < 0) ^ (b < 0)
    # Use absolute values to simplify calculations
    dividend = abs(a)
    divisor = abs(b)
    quotient = 0
    # Perform bit manipulation to find the quotient
    while dividend >= divisor:
        temp = divisor
        multiple = 1
        # Double the divisor until it exceeds the dividend
        while (temp << 1) <= dividend:
            # Double the divisor
            temp <<= 1
            # Double the multiplier
            multiple <<= 1
        # Subtract the largest shifted divisor
        dividend -= temp
        # Add the corresponding multiple to the quotient
        quotient += multiple
    # Apply the sign to the result
    if negative:
        quotient = -quotient
    # Clamp the result to the 32-bit integer range
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
