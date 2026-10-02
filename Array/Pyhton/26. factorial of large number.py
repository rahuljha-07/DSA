# 26. Factorial of a Large Number Using a Digit Array
# Store each decimal digit separately and perform multiplication manually.


def multiply(x, result):
    carry = 0

    # Digits are stored in reverse order: units digit first.
    for i in range(len(result)):
        product = result[i] * x + carry
        result[i] = product % 10  # Keep the last digit.
        carry = product // 10    # Carry the remaining digits forward.

    # Add any digits still left in the carry.
    while carry:
        result.append(carry % 10)
        carry //= 10


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")

    result = [1]

    for x in range(2, n + 1):
        multiply(x, result)

    # Convert from units-first order to normal reading order.
    result.reverse()
    return result


if __name__ == "__main__":
    n = 100
    result = factorial(n)

    print(f"Factorial of {n} is:", end=" ")
    for digit in result:
        print(digit, end="")
    print()

    # Smaller example:
    print("Digits of 5!:", factorial(5))
    # Output: Digits of 5!: [1, 2, 0]


# ---------------------------------------------------------------------------
# HOW IT WORKS
# ---------------------------------------------------------------------------
# Factorial:
# n! = 1 × 2 × 3 × ... × n.
# Both 0! and 1! equal 1.
#
# Store digits backward to process multiplication from units to higher places.
# Example: 120 is stored as [0, 2, 1].
#
# Example: multiply 24 by 5.
# Initially, result = [4, 2], representing 24.
#
# i = 0:
# product = 4 × 5 + 0 = 20.
# result[0] = 20 % 10 = 0.
# carry = 20 // 10 = 2.
#
# i = 1:
# product = 2 × 5 + 2 = 12.
# result[1] = 12 % 10 = 2.
# carry = 12 // 10 = 1.
#
# Carry remains:
# Append 1.
# result = [0, 2, 1], representing 120.
#
# Keep this reverse order during all multiplications.
# Reverse only once, after calculating the complete factorial.
#
# Python's // performs integer floor division.
# Using / would produce a float, which is incorrect for this carry logic.
#
# Python already supports arbitrary-size integers, so this digit-array
# technique is not required to avoid fixed-width integer overflow.
# Here we use it to follow your C++ algorithm and learn manual multiplication.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n² log n)
# ---------------------------------------------------------------------------
# Time complexity describes how work grows with n.
# This analysis treats arithmetic on each digit and carry as O(1),
# as in the usual word-operation model.
#
# Let D be the number of decimal digits in n!.
# Each multiplication scans the digits currently stored.
# There are n - 1 multiplications, and each processes at most D digits.
#
# Therefore, O(n × D) is an upper bound.
#
# The number of digits in n! grows as Θ(n log n).
# Substituting D gives:
# O(n × n log n) = O(n² log n).
#
# Reversing the final D digits takes O(D), which does not dominate.
#
# It is NOT O(n²) simply because there are nested loops:
# the inner loop scans factorial DIGITS, not just n elements.
#
# Exact bit-level analysis would also account for the growing size of x
# and carry in Python's arbitrary-size integer arithmetic.


# ---------------------------------------------------------------------------
# SPACE COMPLEXITY: O(D) = O(n log n)
# ---------------------------------------------------------------------------
# The result list stores D digits of n!.
# Carry and index variables require a fixed number of additional variables.
#
# Including the returned digit list: O(D) space.
# Auxiliary space beyond that list: O(1) in the word-operation model.

'''
Time Complexity: O(n * d), where d is the number of digits in n!

Reason:
For every multiplier from 2 to n, the multiply function scans all digits
currently stored in the result. The digit count grows up to d.

Space Complexity: O(d)

Reason:
The result list stores every digit of n!. Other variables are constant.
'''
