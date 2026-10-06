def findMinOps(arr):
    # Assumes positive integers. Merge a copy, as in C++ pass-by-value.
    arr = list(arr)
    # Count of merge operations
    ans = 0
    # Size of the array
    n = len(arr)
    i = 0
    j = n - 1

    # Use two pointers to process the array
    while i <= j:
        # Equal ends: move both pointers inward.
        if arr[i] == arr[j]:
            i += 1
            # Move the right pointer inward
            j -= 1

        # Left is greater: merge two elements on the right.
        elif arr[i] > arr[j]:
            j -= 1
            # Merge arr[j] and arr[j+1]
            arr[j] += arr[j + 1]
            # Increment the operation count
            ans += 1

        # Right is greater: merge two elements on the left.
        else:
            # Move the left pointer inward
            i += 1
            # Merge arr[i] and arr[i-1]
            arr[i] += arr[i - 1]
            ans += 1

    return ans


arr = [1, 4, 5, 1]
print("Minimum operations to make the array palindrome:", findMinOps(arr))
# Output: Minimum operations to make the array palindrome: 1
# Merge 4 and 5 to get the logical array [1, 9, 1].


# TIME: O(n)
# Each iteration moves at least one pointer inward.
# The pointers cross after at most O(n) iterations.
#
# EXTRA SPACE: O(n)
# The input copy stores n elements; merges use a fixed number of variables.
# The array is not physically shortened; pointers track the active portion.

'''
Time Complexity: O(n)

Reason:
The two pointers move inward after every comparison or merge. They cross
after a linear number of operations.

Space Complexity: O(n)

Reason:
The local input copy stores n elements so the caller's array stays unchanged.
Updating that copy uses only O(1) more space for pointers and the counter.
'''
