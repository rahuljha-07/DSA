# Function to check if the factorial of a number `p` has at least `n` trailing zeroes
def hasAtLeastNTrailingZeroes(number, requiredZeroes):
    # Store the original number for calculations
    temp = number
    # Counter for trailing zeroes
    count = 0
    # Initial factor for trailing zeroes calculation
    factor = 5

    # Count the number of trailing zeroes contributed by factors of 5
    while factor <= temp:
        # Count how many multiples of `factor` are in `temp`
        count += temp // factor
        # Move to the next power of 5
        factor *= 5

    # Return true if the count of trailing zeroes is at least `requiredZeroes`
    return count >= requiredZeroes


# Function to find the smallest number whose factorial contains at least `n` trailing zeroes
def findSmallestFactorialNumberWithTrailingZeroes(n):
    # Special case: If n is 1, the smallest number is 5 (since 5! has 1 trailing zero)
    if n == 1:
        return 5

    # Lower bound for binary search
    low = 0
    # Upper bound for binary search
    high = 5 * n
    # Variable to store the result
    result = -1

    # Binary search to find the smallest number with at least `n` trailing zeroes
    while low < high:
        # Calculate the middle point
        mid = (low + high) // 2
        if hasAtLeastNTrailingZeroes(mid, n):
            # Store candidate
            result = mid
            # If mid has at least n trailing zeroes, search in the left half
            high = mid
        else:
            # Otherwise, search in the right half
            low = mid + 1

    # Return the smallest number found
    return low


n = 6
result = findSmallestFactorialNumberWithTrailingZeroes(n)
print("The smallest number whose factorial has at least", n, "trailing zeroes is:", result)


'''
Time Complexity: O(log n * log n)

Reason:
Binary search is done from 0 to 5n. For each mid, trailing zeroes are counted
by powers of 5, which takes O(log n) divisions.

Space Complexity: O(1)

Reason:
Only count, factor, and binary-search variables are used.
'''
