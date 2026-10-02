def subarray_with_max_product(arr):
    if not arr:
        raise ValueError("The array must not be empty.")

    prefix = 1
    suffix = 1
    answer = arr[0]
    n = len(arr)

    for i in range(n):
        # Start fresh after a zero from the previous iteration.
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1

        # Build products from both directions.
        prefix *= arr[i]
        suffix *= arr[n - i - 1]

        answer = max(answer, prefix, suffix)

    return answer


if __name__ == "__main__":
    arr = [2, 3, -2, 4]

    print("Maximum product:", subarray_with_max_product(arr))
    # Output: Maximum product: 6
    # Subarray: [2, 3].

    print(subarray_with_max_product([-2, 0, -1]))  # 0
    print(subarray_with_max_product([-2, 3, -4]))  # 24
    print(subarray_with_max_product([-5]))        # -5


# ---------------------------------------------------------------------------
# HOW IT WORKS
# ---------------------------------------------------------------------------
# Zeros divide the array into separate nonzero segments.
# Within each segment:
#
# 1. An even number of negatives gives a positive total product.
#    Since nonzero integers have absolute value >= 1, taking the whole
#    segment gives a maximum product for that segment.
#
# 2. An odd number of negatives gives a negative total product.
#    To obtain a positive product, we can exclude:
#    - The prefix through the first negative, OR
#    - The suffix starting at the last negative.
#
# Scanning from both ends considers both choices.
# A segment containing only one negative element is also handled:
# that element itself is checked.
#
# Example: [2, 3, -2, 4]
#
# i = 0: prefix = 2,   suffix = 4,   answer = 4.
# i = 1: prefix = 6,   suffix = -8,  answer = 6.
# i = 2: prefix = -12, suffix = -24, answer = 6.
# i = 3: prefix = -48, suffix = -48, answer = 6.
#
# Why reset a zero product to 1?
# Otherwise, all later multiplications would remain 0.
# The reset lets us start a new segment after the zero.
#
# Zero itself is still considered:
# multiplying by it produces 0, and answer is updated BEFORE the next reset.
#
# Why initialize answer to arr[0] instead of 0?
# For [-5], the correct answer is -5; an empty subarray is not allowed.
#
# This prefix/suffix method relies on integer inputs.
# Arbitrary fractions between -1 and 1 require a different approach,
# such as tracking maximum and minimum products ending at each position.
#
# The function returns the product, not the subarray.
# The original array is not modified.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n)
# ---------------------------------------------------------------------------
# Time complexity describes how work grows with input size n.
#
# One loop runs n times.
# Each iteration performs two multiplications, comparisons, and resets.
# Under the usual constant-time arithmetic model:
#
# Total work = n × O(1) = O(n).
#
# Scanning from both ends inside the same loop does not make it O(n²).


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(1)
# ---------------------------------------------------------------------------
# Only a fixed number of variables are used.
# No additional list or recursion is needed.
#
# Therefore, extra space is O(1) under the usual word-operation model.
#
# Python integers can grow as the products grow. Exact bit-level time
# and memory costs depend on the number of digits in those products.

'''
Time Complexity: O(n)

Reason:
The array is scanned once while maintaining prefix and suffix products.
Each iteration performs constant work.

Space Complexity: O(1)

Reason:
Only prefix, suffix, answer, and index variables are used.
'''
